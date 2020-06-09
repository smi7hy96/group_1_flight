from plane_class import Plane
from FlightTrip import FlightTrip
from passenger import Passenger

plane = Plane("AirSparta",20,20,15,10)
seats = plane.get_seats()
flight = FlightTrip(1,"Peru","12/06/2020","2:00PM",20,20)

michael = Passenger("Michael", "111", 21, "21/12/1992")
samir = Passenger("Samir", "122", 23, "21/12/1999")

flight.add_passenger_to_flight(michael)
flight.add_passenger_to_flight(samir)

# print(flight.return_passenger_list())

# flight.remove_passenger_from_flight(122)

# print(flight.return_passenger_list())

print(flight.flight_attendee_report())






