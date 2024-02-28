"""7.write a python program to send an email with multiple recipients using the smtplib library."""

import smtplib
from email.mime.text import MIMEText

def send_email(sender_email, receiver_emails, message, subject):

    try:
        # Replace these with your actual credentials and consider using environment variables for security
        smtp_server = "smtp.example.com"
        port = 587  

        # Create a MIMEText object with the email content
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = ", ".join(receiver_emails)  

    
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()

            # Authenticate with the SMTP server using credentials (consider using secure authentication methods)
            server.login(sender_email, "your_password")

            # Send the email to all recipients
            server.sendmail(sender_email, receiver_emails, msg.as_string())
            print(f"Email sent successfully to {', '.join(receiver_emails)}!")

    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")


sender_email = "sender@example.com"
receiver_emails = ["receiver1@example.com", "receiver2@example.com"]
message = "This is an email sent to multiple recipients using Python's smtplib library."
subject = "Email with Multiple Recipients"

send_email(sender_email, receiver_emails, message, subject)
