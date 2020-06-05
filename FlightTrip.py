class FlightTrip:

    def __init__(self, flight_number, destination, flight_date, flight_time, seats, available_seats, ticket_price,
                 passenger_list=None):
        if passenger_list is None:
            passenger_list = []
        self.flight_number = flight_number
        self.destination = destination
        self.flight_date = flight_date
        self.flight_time = flight_time
        self.seats = seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price

    def return_passenger_list(self):
        for passenger in self.passenger_list:
            return passenger