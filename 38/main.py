import requests
import creds
from datetime import datetime
import base64
import os

GENDER = "male"
WEIGHT_KG = 131
HEIGHT_CM = 173
AGE = 48

exercise_done = input("Tell me which exercises you did: ")
entry_date = datetime.now()


headers = {
    "X-APP-ID":os.environ.get('APP_ID'),
    "X-APP-KEY":os.environ.get('API_KEY')
}
nutritionix_payload = {
    "query": exercise_done,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
nutritionix_api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(url=nutritionix_api_endpoint, headers=headers, json=nutritionix_payload).json()
print(response["exercises"][0]["name"])

sheety_api_write_endpoint = os.environ.get('SHEET_ENDPOINT')

print(entry_date.strftime('%d/%m/%Y'))
print(entry_date.strftime('%H:%M/%S'))
sheety_token = os.environ.get('TOKEN')
sheety_key_enc = base64.b64encode(sheety_token.encode()).decode()
sheety_headers = {
    "Authorization": "Bearer " + sheety_key_enc
}
for exercise in response["exercises"]:
    sheety_payload = {
        "workout": {
            "date": entry_date.strftime('%d/%m/%Y'),
            "time": entry_date.strftime('%X'),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    response = requests.post(url=sheety_api_write_endpoint, json=sheety_payload, headers=sheety_headers)
    print(response.json())
    print(response.text)
    print(response)