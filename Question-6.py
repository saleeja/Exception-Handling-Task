"""6.Write a Python program that reads email details (sender, recipient, subject, and body) from user input and sends the email using Mailtrap as the SMTP server.
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    
    sender_email = input("Enter your email address (sender): ")
    recipient_email = input("Enter recipient's email address: ")
    subject = input("Enter the email subject: ")
    body = input("Enter the email body: ")

    # Mailtrap SMTP server details
    smtp_server = "smtp.mailtrap.io"
    smtp_port = 465
    smtp_username = "your_mailtrap_username"
    smtp_password = "your_mailtrap_password"

    # Create the MIMEText object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        # Establish a connection to the Mailtrap SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Login to the SMTP server using your Mailtrap credentials
            server.login(smtp_username, smtp_password)

            server.sendmail(sender_email, recipient_email, message.as_string())

        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print(f"Error: Unable to send email - {e}")

if __name__ == "__main__":
    send_email()
