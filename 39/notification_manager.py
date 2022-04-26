from twilio.rest import Client
import creds
from flight_data import FlightData
from datetime import datetime

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def send_message(data: FlightData):
        client = Client(creds.account_sid, creds.auth_token)
        message_body = f"Low price alert! Only £{data.ticket_price} to fly from {data.depart_city}-{data.depart_iata} to {data.dest_city}-{data.dest_iata}, from {data.depart_date} to {data.return_date}"

        message = client.messages.create(
                            body=message_body,
                            from_='+13344715177',
                            to=creds.my_phone_number
        )
        return message