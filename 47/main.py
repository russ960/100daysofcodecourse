from pydoc import resolve
import requests
from bs4 import BeautifulSoup
import lxml
import creds
import smtplib
from email.mime.text import MIMEText

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

headers = {
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
}

url = "https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/ref=dp_fod_1?pd_rd_i=B08PQ2KWHS&th=1"

response = requests.get(url, headers=headers).text
# print(response)
soup = BeautifulSoup(response, "lxml")
output = soup.find(name="span", class_="a-offscreen")
price = float(output.text.split('$')[1])
print(price)

product_title = (soup.find(id="productTitle").text).strip()
email_subject = f"{product_title} price alert!"
email_body = f"The price for the Instant Pot Pro 10-in-1 Pressure Cooker is currently at ${price}"

if price < 100.00:
    send_mail(creds.my_email, creds.pers_email, email_subject, email_body)