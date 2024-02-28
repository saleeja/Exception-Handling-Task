"""7.write a python program to send an email with multiple recipients using the smtplib library."""

import smtplib
from email.mime.text import MIMEText

def send_email():
    sender_email = "saleejas2@gmail.com"
    recipients = ["receiver1@gmail.com", "receiver2@gmail.com"]  # List of recipient email addresses
    subject = "Mailtrap"
    body = """Mailtrap is a service that allows developers to test and debug their email functionality in  safe and isolated environment.It provides a fake SMTP server that can beused to capture and inspect outgoing emails from your application without actually sending them to the intended recipients"""

    # Mailtrap SMTP server details
    smtp_server = "sandbox.smtp.mailtrap.io"
    smtp_port = 2525
    smtp_username = "64941c4047d48b"
    smtp_password = "aeafd5888df080"

    try:
        # Create the MIMEText object
        message = MIMEText(body)
        message['From'] = sender_email
        message['To'] = ", ".join(recipients)  # Join recipient emails with commas
        message['Subject'] = subject

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)

        # Start TLS
        server.starttls()

        # Login to the SMTP server using your Mailtrap credentials
        server.login(smtp_username, smtp_password)

            # Send the email
        server.sendmail(sender_email, recipients, message.as_string())
        print("Email sent successfully.")

    except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")

    finally:
            # Quit the server in the 'finally' block to ensure it's done even if there was an exception
            server.quit() if 'server' in locals() else None

send_email()
