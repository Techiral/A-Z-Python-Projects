import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to get the latest Hacker News headlines
def get_hacker_news_headlines():
    url = 'https://news.ycombinator.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = []
    
    for item in soup.find_all('a', class_='storylink'):
        headlines.append(item.text)
    
    return headlines

# Function to send an email
def send_email(subject, body, to_email):
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    smtp_port = 587
    smtp_user = 'your_email@example.com'  # Replace with your email
    smtp_password = 'your_password'  # Replace with your email password

    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to_email, msg.as_string())
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print('Email could not be sent. Error:', str(e))

# Main function
if __name__ == '__main__':
    # Get the latest Hacker News headlines
    headlines = get_hacker_news_headlines()
    
    # Construct the email message
    subject = 'Latest Hacker News Headlines'
    body = '\n'.join(headlines)

    # Replace with your recipient's email address
    recipient_email = 'recipient@example.com'

    # Send the email
    send_email(subject, body, recipient_email)

