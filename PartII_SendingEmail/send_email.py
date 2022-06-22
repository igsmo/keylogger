import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import datetime

# Create message
sender_password = "VeryRealPassword"
sender_address = "ottercomp@outlook.com"

message = MIMEMultipart()
message["From"] = sender_address
message["To"] = sender_address
message["Subject"] = "Auto"

content = open('log_file.txt', 'r').read()

message.attach(MIMEText(content, 'plain'))

# Send an email
session = smtplib.SMTP('smtp.office365.com', 587)
session.starttls()
session.login(sender_address, sender_password)
session.sendmail(sender_address, sender_address, message.as_string())
session.quit()
