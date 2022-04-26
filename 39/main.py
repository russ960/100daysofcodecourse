import data_manager
import flight_search
from datetime import datetime, timedelta        
from notification_manager import NotificationManager              
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

worksheet = data_manager.DataManager().get_worksheet()
begin_date = (datetime.now() + timedelta(days = 2)).strftime('%d/%m/%Y')
end_date = (datetime.now() + timedelta(days = 28)).strftime('%d/%m/%Y')

for row in worksheet:
    if row["iataCode"] == '':
        # print(flight_search.FlightSearch().get_iata_code(row["city"]))
        data_manager.DataManager.update_iata(id = row["id"], iata_code = flight_search.FlightSearch().get_iata_code(row["city"]))

    flight_data = flight_search.FlightSearch().search_flight_cost(depart_iata = "LON", destination_iata = row['iataCode'], start_date = begin_date, stop_date = end_date)

    if flight_data is not None:
        print(flight_data.depart_iata)
        if flight_data.ticket_price < row["lowestPrice"] and flight_data.dest_iata == row["iataCode"]:
            # print(f"flyFrom: {flight_data.depart_iata}  flyTo: {row['iataCode']}  Price: £{flight_data.ticket_price}")
            NotificationManager.send_message(flight_data)
