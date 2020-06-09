from passenger import *

class FlightTrip:

    def __init__(self, flight_number: object, destination: object, flight_date: object, flight_time: object, seats: object, available_seats: object,
                 passenger_list: object = None) -> object:
        if passenger_list is None:
            self.passenger_list = []
        self.flight_number = flight_number
        self.destination = destination
        self.flight_date = flight_date
        self.flight_time = flight_time
        self.seats = seats
        self.available_seats = available_seats

    def return_passenger_list(self):
        return self.passenger_list

    def ticket_revenue(self):
        total_revenue = 0
        for person in self.passenger_list:
            total_revenue += person.passenger_price
        return total_revenue

    def add_passenger(self, passenger):
        if self.available_seats == 0:
            return "Sorry we are fully booked. Choose another flights or wait to see cancellations."
        else:
            self.passenger_list.append(passenger)
            self.available_seats -= 1
            return f'{passenger.name} added to flight!'

    def remove_passenger(self, passport_number):
        for passenger in self.passenger_list:
            if passenger.passport_no == passport_number:
                self.passenger_list.remove(passenger)
                self.available_seats += 1
                return f'{passenger.name} removed from flight.'

    def flight_attendee_report(self):
        for passenger in self.passenger_list:

            return f"Name: {passenger.name}, Passport Number: {passenger.get_passport_no()}"

            print(f"Name: {passenger.name}, Passport Number: {passenger.passport_no}")

    def add_passenger_to_flight(self, michael):
        pass


