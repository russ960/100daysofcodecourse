##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# Done

# 2. Check if today matches a birthday in the birthdays.csv
# Done

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# Done

# 4. Send the letter generated in step 3 to that person's email address.
# Done

from operator import index
import pandas as pd
import datetime as dt
from random import randint
import smtplib
from email.mime.text import MIMEText
import creds

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

data = pd.read_csv('.\\32\\birthday\\birthdays.csv', index_col=None)
data_dict = data.to_dict(orient='records')

current_month = dt.datetime.now().month
current_day = dt.datetime.now().day

for row in data_dict:
    if row['month'] == current_month and row['day'] == current_day:
        letter_file = f".\\32\\birthday\\letter_templates\\letter_{randint(1,3)}.txt"
        with open(letter_file, mode='r') as letter_template:
            letter = letter_template.read()
        letter = letter.replace('[NAME]',row['name'])
        send_mail(creds.my_email, creds.pers_email, "Happy Birthday", letter)