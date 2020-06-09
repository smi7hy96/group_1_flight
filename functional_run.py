from people import People
from plane_class import Plane
from FlightTrip import FlightTrip
from passenger import Passenger

flight_cannes = FlightTrip(1, 'Cannes', '01/01/2022', '10:00', 3, 3)

while True:
    pass_or_staff = input("Passenger or Staff? ")
    if pass_or_staff.lower() == 'staff':
        break

    elif pass_or_staff.lower() == 'passenger':
        name = input("Enter name: ")
        tax_no = input('Enter tax number: ')
        passport_no = input("Enter passport number: ")
        dob = input("Enter date of birth: ")
        with_child = input("Are you travelling with infant? [True/False]")
        if with_child == 'True':
            with_child = True
        elif with_child == 'False':
            with_child = False

        pass1 = Passenger(name, tax_no, passport_no, dob, with_child)

        flight_options = input("Where do you want to go? ")
        if flight_options.capitalize() == flight_cannes.destination:
            print(flight_cannes.add_passenger(pass1))

    else:
        print('Invalid response')
        break
    flight_cannes.flight_attendee_report()
    print(flight_cannes.ticket_revenue())



