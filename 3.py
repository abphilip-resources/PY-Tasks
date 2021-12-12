import smtplib

s = 'YOUR_EMAIL@EMAIL.COM'               
p = 'YOUR_PASSWORD'                   

def email(r, subject, body):
    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(s, p)
        server.sendmail(s, r, message)

email('allenbphilip@gmail.com', 'Notification', 'Everything is awesome!')