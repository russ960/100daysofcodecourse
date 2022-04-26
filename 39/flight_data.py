class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, destination_iata, destination_city, depart_iata, depart_city, depart_date, return_date, price):
        self.dest_iata = destination_iata
        self.dest_city = destination_city
        self.depart_iata = depart_iata
        self.depart_city = depart_city
        self.depart_date = depart_date
        self.return_date = return_date
        self.ticket_price = price
