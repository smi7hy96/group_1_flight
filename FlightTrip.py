from passenger import *

class FlightTrip:

    def __init__(self, flight_number, destination, flight_date, flight_time, seats, available_seats, ticket_price, passenger_list=None):
        self.flight_number = flight_number
        self.destination = destination
        self.flight_date = flight_date
        self.flight_time = flight_time
        self.seats = seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price

        if self.passenger_list is None:
            self.passenger_list = []

    def return_passenger_list(self):
        for passenger in self.passenger_list:
            return passenger


    def add_to_flight(self, passenger):
        self.adult_list = []
        self.infant_list = []

        if passenger.adult == True:
            self.adult_list.append(passenger)

        else:
            self.infant_list.append(passenger)


    def attendees_list(self):
        self.passenger_list = self.adult_list + self.infant_list


    def ticket_total(self, price):
        total_revenue = 0
        for person in self.passenger_list:
            self.total_revenue += price.passenger_price
        return total_revenue
