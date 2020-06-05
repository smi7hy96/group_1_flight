from plane_class import Plane
from FlightTrip import FlightTrip

plane = Plane("AirAfrica",300,50,40,25)
seats = plane.get_seats()
flight = FlightTrip(1,"Morocco","07/06/2020","2:00PM", seats, seats,plane.get_adult_price())

print(flight.seats)





