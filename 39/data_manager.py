from mimetypes import init
import requests
import creds

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass
    
    def get_worksheet(self):
        sheety_headers = {
            "Authorization": "Bearer " + creds.sheety_key
        }
        response = requests.get(creds.sheet_location,headers=sheety_headers)
        return response.json()["prices"]
    
    def update_iata(id, iata_code):
        update_url = creds.sheet_location + "/" + str(id)
        print(update_url)
        sheety_headers = {
            "Authorization": "Bearer " + creds.sheety_key
        }
        # print(f"iataCode: {iata_code}")
        payload = {
            "price": {
                "iataCode": iata_code 
            }           
        }
        response = requests.put(update_url,headers=sheety_headers, json=payload)
        print(response.text)