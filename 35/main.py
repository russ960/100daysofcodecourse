import requests
import creds
from twilio.rest import Client

parameters = {
    "lat": 35.149532,
    "lon": -90.048981,
    "appid": creds.weather_api_key,
    "exclude": "current,minutely,daily"
}
api_url = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(api_url,params=parameters)
response.raise_for_status()

# print(response.status_code)
hourly = response.json()["hourly"]
weather_slice = []
weather_slice = hourly[0:12]
will_rain = False
for hour in weather_slice:
    condition_code = int(hour["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain == True:
    client = Client(creds.account_sid, creds.auth_token)

    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring an ☂️",
                        from_='+13344715177',
                        to=creds.my_phone_number
                    )
    print(message.status)