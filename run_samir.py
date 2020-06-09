from plane_class import Plane
from FlightTrip import FlightTrip
from passenger import Passenger

# Defining stuff
samir = Passenger("Samir", "15503", 122, "24/08/1999")
stefan = Passenger('Stefan', '123A', 100, '10/12/96')
ryan = Passenger('Ryan', '2468B', 555, '08/06/20')
mergim = Passenger('Mergim', '101010X', 777, '01/01/2077')

flight1 = FlightTrip(1, 'Egypt', '01/01/2022', '10:00', 3, 3)
flight2 = FlightTrip(2, 'Peru', '01/01/2022', '12:00', 3, 3)
flight3 = FlightTrip(3, 'Spain', '01/01/2022', '2:00', 3, 3)

# User program
while True:
    print("Welcome to Sparta Airport, where we fly Global.")
    user = input("What is your username? ")

    if user == "samir":
        user = samir
    elif user == "stefan":
        user = stefan
    elif user == "ryan":
        user = ryan
    elif user == "mergim":
        user = mergim
    else:
        print("We have no current user matching that username")
        break

    print(f"What would you like to do today {user.name}?")
    choice = input("1: Book a Flight. 2: View flight details. ")
    # Book a flight
    if choice == "1":

        ongoing_flights = [flight1, flight2, flight3]

        print(f"We currently have {len(ongoing_flights)} ongoing flights. ")
        for flight in ongoing_flights:
            print (f"{flight.flight_number}: {flight.destination}")

        flight_concern = input("Which flight are you interested in today? [1,2,3] ")
        if flight_concern == "1":
            flight1.add_passenger(user)
            print("We have booked that for you. Enjoy your flight! ")
        elif flight_concern == "2":
            flight2.add_passenger(user)
            print("We have booked that for you. Enjoy your flight! ")
        elif flight_concern == "3":
            flight3.add_passenger(user)
            print("We have booked that for you. Enjoy your flight! ")
    # Flight details
    elif choice == "2":

        ongoing_flights = [flight1, flight2, flight3]

        print(f"We currently have {len(ongoing_flights)} ongoing flights. ")
        for flight in ongoing_flights:
            print(f"{flight.flight_number}: {flight.destination}")
        selected = input("Which flight are you interested in today? [1,2,3] ")
        if selected == "1":
            print(flight1.flight_attendee_report())
        elif flight_concern == "2":
            print(flight2.flight_attendee_report())
        elif flight_concern == "3":
            print(flight3.flight_attendee_report())

