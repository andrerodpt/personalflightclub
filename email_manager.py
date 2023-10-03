import smtplib
from credentials import MY_EMAIL, EMAIL_PASSWORD, SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(email, msg):
    with smtplib.SMTP(SMTP) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)

        email_message = MIMEMultipart()
        email_message['Subject'] = 'FLIGHT DEAL!'
        email_message['From'] = MY_EMAIL
        email_message['To'] = email

        text_body = MIMEText(msg, 'plain', 'utf-8')
        email_message.attach(text_body)

        print(email)
        print(email_message)
        # connection.sendmail(
        #     from_addr=MY_EMAIL, 
        #     to_addrs=email, 
        #     msg=email_message.as_string()
        # )

def send_emails(users_list, msg):
    print(users_list['users'])
    for user in users_list['users']:
        print(user)
        send_email(user['email'], msg)