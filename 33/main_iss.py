from time import sleep
import requests
from datetime import datetime, timedelta
import creds
import smtplib
from email.mime.text import MIMEText

YAHOO_ACCOUNT = creds.my_email
YAHOO_PASS = creds.password
MY_LAT =  51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

def send_mail():
    fromAddr = creds.my_email
    toAddrs = creds.pers_email
    subject = "ISS is visable"
    body = "ISS should be visable."
    msg = MIMEText(body)
    msg['From'] = fromAddr
    msg['To'] = toAddrs
    msg['Subject'] = subject
    with smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) as connection:
        connection.ehlo()
        connection.login(YAHOO_ACCOUNT, YAHOO_PASS)
        connection.sendmail(fromAddr, toAddrs, msg.as_string())

#Your position is within +5 or -5 degrees of the ISS position.
def is_iss_nearby(latitude, longitude):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if iss_latitude >= latitude-5.0 and iss_latitude <= latitude+5.0:
        if iss_longitude >= longitude-5.0 and iss_longitude <= longitude+5.0:
            return True


def is_night():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if time_now.hour > sunset or time_now.hour < sunrise:
        return True

while True:
    if is_night() and is_iss_nearby(MY_LAT, MY_LONG):
        send_mail()
    sleep(60)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




