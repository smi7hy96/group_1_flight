from plane_class import Plane
from FlightTrip import FlightTrip
from passenger import Passenger
from people import People

plane = Plane("AirSparta",20,20,15,10)
seats = plane.get_seats()
flight = FlightTrip(1,"Peru","12/06/2020","2:00PM",20,20)

michael = Passenger("Michael", "111", 21, "21/12/1992")
samir = Passenger("Samir", "122", 23, "21/12/1999")

flight.add_passenger(michael)
flight.add_passenger(samir)

# print(flight.return_passenger_list())

flight = FlightTrip(1, 'Bora Bora', '01/01/2022', '10:00', 3, 3)

samir = Passenger("Samir", "15503", 122, "24/08/1999")
stefan = Passenger('Stefan', '123A', 100, '10/12/96')
ryan = Passenger('Ryan', '2468B', 555, '08/06/20', True)
mergim = Passenger('Mergim', '101010X', 777, '01/01/2077')


print(flight.add_passenger(samir))
print(flight.add_passenger(stefan))
print(flight.add_passenger(ryan))
print(flight.add_passenger(mergim))

flight.flight_attendee_report()
print(flight.return_passenger_list())

print(flight.remove_passenger(122))

print(flight.add_passenger(mergim))

flight.flight_attendee_report()

# print(flight.return_passenger_list())

print(flight.ticket_revenue())






