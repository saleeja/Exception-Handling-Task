
"""8.write a python program to handle exceptions when sending emails using Python's smtplib library."""



import smtplib
from email.mime.text import MIMEText

def send_email(sender_email, receiver_email, message, subject):
  """
  Sends an email with proper exception handling.

  Args:
      sender_email: Email address of the sender.
      receiver_email: Email address of the receiver.
      message: The body content of the email.
      subject: The subject line of the email.

  Raises:
      SMTPException: If an error occurs during the email sending process.
  """

  try:
    # Replace these with your actual credentials
    smtp_server = "smtp.example.com"
    port = 587  # Use 465 for SSL/TLS

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP(smtp_server, port) as server:
      server.starttls()
      server.login(sender_email, "your_password")
      server.sendmail(sender_email, receiver_email, msg.as_string())
      print("Email sent successfully!")

  except smtplib.SMTPException as e:
    print(f"Error sending email: {e}")

# Example usage
sender_email = "sender@example.com"
receiver_email = "receiver@example.com"
message = "This is an email sent using Python's smtplib library."
subject = "Test Email"

send_email(sender_email, receiver_email, message, subject)
