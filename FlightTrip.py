class FlightTrip:

    def __init__(self, flight_number, destination, flight_date, flight_time, seats, available_seats, ticket_price,
                 passenger_list=None):
        if passenger_list is None:
            self.passenger_list = []
        self.flight_number = flight_number
        self.destination = destination
        self.flight_date = flight_date
        self.flight_time = flight_time
        self.seats = seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price

    def return_passenger_list(self):
        for passenger in self.passenger_list:
            return passenger.name

    def add_passenger_to_flight(self, passenger):
        if self.available_seats == 0:
            return "Sorry we are fully booked. Choose another flights or wait to see cancellations."
        else:
            self.passenger_list.append(passenger)
            self.available_seats -= 1

    def remove_passenger_from_flight(self, passport_number):
        for passenger in self.passenger_list:
            if passenger._passport_no == passport_number:
                self.passenger_list.remove(passenger)

        self.available_seats += 1

    def flight_attendee_report(self):
        for passenger in self.passenger_list:
            return f"Name: {passenger.name}, Passport Number: {passenger._passport_no}"
