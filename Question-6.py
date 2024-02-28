"""6.Write a Python program that reads email details (sender, recipient, subject, and body) from user input and sends the email using Mailtrap as the SMTP server.
"""
import smtplib
from email.mime.text import MIMEText

def send_email():
    sender_email = "saleejas2@gmail"
    recipient_email = "receiver@gmail.com"
    subject = " the email subject: "
    body = " the email body: "

    # Mailtrap SMTP server details
    smtp_server = "sandbox.smtp.mailtrap.io"
    smtp_port = 2525
    smtp_username = "64941c4047d48b"
    smtp_password = "aeafd5888df080"


    try:
        # Create the MIMEText object
        message = MIMEText(body)
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)

        # Start TLS
        server.starttls()

        # Login to the SMTP server using your Mailtrap credentials
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())
        print("Email sent successfully.")

    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

    finally:
        
        server.quit() if 'server' in locals() else None

send_email()



