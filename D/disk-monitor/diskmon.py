import subprocess
import re
import yagmail
import smtplib
import syslog

# --- START CONFIG --- #
USERNAME = {'YOUR GMAIL USERNAME': 'NICKNAME'}
PASSWORD = 'YOUR GMAIL PASSWORD'
ALERT_RECIPIENT = 'THE RECIPIENT EMAIL ADDRESS'
# --- END CONFIG --- #


class DiskMonitorError(Exception):
    pass


class DiskMonitor:
    def __init__(self, gmail_username, gmail_password, alert_recipient, partition, threshold):
        self.gmail_username = gmail_username
        self.gmail_password = gmail_password
        self.alert_recipient = alert_recipient
        self.partition = partition
        self.threshold = threshold

    def _convert_bytes(self, size):
        ''' Converts the input size (in KB) into a more readable format '''
        for x in ['KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return f'{size:3.1f} {x}'
            size /= 1024.0
        return f'{size:,}'

    def _get_disk_space(self):
        ''' Returns the available disk space (in KB) and its percentage utilization '''

        # Get the disk utilization data from the command 'df'.
        try:
            out = subprocess.run(
                ['df'], check=True, capture_output=True, text=True
            )
        except subprocess.SubprocessError as e:
            raise DiskMonitorError(f'Failed to measure disk space: {e}')

        # Parse the output to get the available space and the percentage of disk
        # utilization of the specified disk partition.
        parsed = re.search(
            f'.* (\d+) .* (\d+)%.*{self.partition}\\n', out.stdout
        )
        if parsed is None:
            raise DiskMonitorError('Failed to parse "df" output')

        return int(parsed.group(1)), int(parsed.group(2))

    def _send_alert(self, available, use):
        ''' Send an email alert to the specified recipient '''
        out = subprocess.run(['hostname'], capture_output=True, text=True)
        if out.stdout is not None:
            hostname = out.stdout.capitalize()
        else:
            hostname = '[Unknown server]'

        subject = f'{hostname} disk space alert'
        contents = [
            f'Disk space utilization over {use}%.',
            f'Only {self._convert_bytes(available)} left.'
        ]
        try:
            yag = yagmail.SMTP(self.gmail_username, self.gmail_password)
            yag.send(self.alert_recipient, subject, contents)
        except (
            smtplib.SMTPException,
            smtplib.SMTPAuthenticationError,
            yagmail.error.YagConnectionClosed,
            yagmail.error.YagAddressError,
            yagmail.error.YagInvalidEmailAddress,
        ) as e:
            raise DiskMonitorError(f'Failed to send email alert: {e}')

    def monitor(self):
        ''' Send an email alert if the disk is almost full'''
        available, use = self._get_disk_space()
        if use >= self.threshold:
            self._send_alert(available, use)


if __name__ == '__main__':
    try:
        DiskMonitor(USERNAME, PASSWORD, ALERT_RECIPIENT, '/', 90).monitor()
    except DiskMonitorError as e:
        syslog.syslog(syslog.LOG_ALERT, str(e))