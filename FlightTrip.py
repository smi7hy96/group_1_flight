from passenger import *

class FlightTrip:

    def __init__(self, flight_number, destination, flight_date, flight_time, seats, available_seats,
                 passenger_list=None):
        if passenger_list is None:
            self.passenger_list = []
        self.flight_number = flight_number
        self.destination = destination
        self.flight_date = flight_date
        self.flight_time = flight_time
        self.seats = seats
        self.available_seats = available_seats
        self.adult_list = []
        self.infant_list = []

    def return_passenger_list(self):
        for passenger in self.passenger_list:
            return passenger

    def add_to_flight(self, passenger):
        if passenger.adult == True:
            self.adult_list.append(passenger)
        else:
            self.infant_list.append(passenger)

    def attendees_list(self):
        self.passenger_list = self.adult_list + self.infant_list

    def ticket_revenue(self):
        total_revenue = 0
        for person in self.passenger_list:
            total_revenue += person.passenger_price
        return total_revenue

    def add_passenger_to_flight(self, passenger):
        if self.available_seats == 0:
            return "Sorry we are fully booked. Choose another flights or wait to see cancellations."
        else:
            self.passenger_list.append(passenger)
            self.available_seats -= 1

    def remove_passenger(self, passport_number):
        for passenger in self.passenger_list:
            if passenger.__passport_no == passport_number:
                self.passenger_list.remove(passenger)

        self.available_seats += 1

    def flight_attendee_report(self):
        for passenger in self.passenger_list:
            return f"Name: {passenger.name}, Passport Number: {passenger.__passport_no}"

