import smtplib
from email.mime.text import MIMEText
import creds

YAHOO_ACCOUNT=creds.my_email
YAHOO_PASS=creds.password    # not your account password

def send_mail(fromAddr, toAddrs, subject, body):
    msg = MIMEText(body)
    msg['From'] = fromAddr
    msg['To'] = toAddrs
    msg['Subject'] = subject
    s = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
    s.ehlo()
    s.login(YAHOO_ACCOUNT, YAHOO_PASS)
    s.sendmail(fromAddr, toAddrs, msg.as_string())
    s.quit()

send_mail(creds.my_email, creds.pers_email, "test", "Test Body")