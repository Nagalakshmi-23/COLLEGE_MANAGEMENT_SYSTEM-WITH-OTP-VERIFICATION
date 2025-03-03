import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

def send_otp1(data):
    
    otp1 = random.randint(1111,9999)

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    username = "nagalakshmimatthurthi23@gmail.com"
    password = "vjmp daqe zfwx ttmu"

    from_email = "nagalakshmimatthurthi23@gmail.com"
    to_email = data
    subject = "OTP Validation"
    body = f"OTP for Validation is {otp1}. \nThank You."

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP(smtp_server,smtp_port)
    server.starttls()
    server.login(username,password)
    server.send_message(msg)
    server.quit()

    return otp1
