import smtplib
from email.mime.text import MIMEText
import creds
import datetime as dt
from random import choice

# Credentials are stored in creds.py which is not in .gitignore
#   creds.my_email - Test email account
#   creds.password - Test email account password
#   creds.pers_email - Personal e-mail

YAHOO_ACCOUNT=creds.my_email
YAHOO_PASS=creds.password

def send_mail(fromAddr, toAddrs, subject, body):
    msg = MIMEText(body)
    msg['From'] = fromAddr
    msg['To'] = toAddrs
    msg['Subject'] = subject
    with smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) as connection:
        connection.ehlo()
        connection.login(YAHOO_ACCOUNT, YAHOO_PASS)
        connection.sendmail(fromAddr, toAddrs, msg.as_string())

with open('.\\32\\quotes.txt', mode='r') as quote_file:
    quotes = quote_file.readlines()
random_quote=''

now = dt.datetime.now()
if now.weekday() == 3:
    random_quote = choice(quotes)
    send_mail(creds.my_email, creds.pers_email, "Inspirational quote of the day", random_quote)

print(random_quote)