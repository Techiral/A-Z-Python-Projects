import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup as bs

def send_mail(email, password, FROM, TO, msg):
    # initialize the SMTP server
    # in our case it's for Microsoft365, Outlook, Hotmail, and live.com
    server = smtplib.SMTP(host="smtp.office365.com", port=587)
    # connect to the SMTP server as TLS mode (secure) and send EHLO
    server.starttls()
    # login to the account using the credentials
    server.login(email, password)
    # send the email
    server.sendmail(FROM, TO, msg.as_string())
    # terminate the SMTP session
    server.quit()


def email_sender(
    sender_email,
    sender_password,
    receiver_email,
    subject
):
    # initialize the message we wanna send
    msg = MIMEMultipart("alternative")
    # set the sender's email
    msg["From"] = sender_email
    # set the receiver's email
    msg["To"] = receiver_email
    # set the subject
    msg["Subject"] = subject
    # set the body of the email as HTML
    html = """
    This email is sent using <b>Python </b>!
    """
    # uncomment below line if you want to use the HTML template
    # located in mail.html
    # html = open("mail.html").read()
    # make the text version of the HTML
    text = bs(html, "html.parser").text

    text_part = MIMEText(text, "plain")
    html_part = MIMEText(html, "html")
    # attach the email body to the mail message
    # attach the plain text version first
    msg.attach(text_part)
    msg.attach(html_part)

    # send the mail
    send_mail(
        sender_email,
        sender_password,
        sender_email,
        receiver_email,
        msg
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Simple Python script to send email")
    parser.add_argument("email", help="email address")
    parser.add_argument("password", help="email password")
    parser.add_argument("subject", help="email subject")
    args = parser.parse_args()
    email_sender(args.email, args.password, args.subject)
