from people import People
from passenger import Passenger
from FlightTrip import FlightTrip

stefan = Passenger('stefan', '123A', True, 567, '10/12/96')
ryan = Passenger('ryan', '456B', False, 112233, '05/06/2020')
mergim = Passenger('mergim', '576', True, 34567745, '01/01/99')

first_flight = FlightTrip(1, 'Madagascar', '01/08/2020', '9am',
                          100, 10)

first_flight.add_to_flight(stefan)
first_flight.add_to_flight(ryan)
first_flight.add_to_flight(mergim)

print(first_flight.infant_list)