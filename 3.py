import os
import ssl
import smtplib
from dotenv import load_dotenv
load_dotenv() 
s = os.getenv('username')              
p = os.getenv('password')             

def email(r, subject, body):
    context = ssl.create_default_context()
    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(s, p)
        server.sendmail(s, r, message)
    server.quit() 

email('allenbphilip@gmail.com', 'Python', 'Everything is awesome!')