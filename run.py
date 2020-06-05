from plane_class import Plane
from FlightTrip import FlightTrip
from passenger import Passenger

plane = Plane("AirAfrica",300,50,40,25)
seats = plane.get_seats()
flight = FlightTrip(1,"Morocco","07/06/2020","2:00PM", seats, seats,plane.get_adult_price())

print(flight.seats)

samir = Passenger("Samir", "15503", True, 122, "24/08/1999")

print(samir._passport_no)

flight.add_passenger_to_flight(samir)

print(flight.return_passenger_list())

# flight.remove_passenger_from_flight(122)

print(flight.return_passenger_list())

print(flight.flight_attendee_report())





