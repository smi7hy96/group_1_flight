import sys
from preset_variables_ryan import *


def exit_system():
    print("Logout Successful")
    sys.exit()


def back_to_passenger():
    print("Aborting process, re-directing back to passenger panel")
    passenger_settings_choice()


def back_to_flight():
    print("Aborting process, re-directing back to flight panel")
    flight_settings_choice()


def print_panel():
    print("ADMIN CONTROL: \n")
    print("1) Passenger Settings")
    print("2) Flight Settings")


def check_if_number(number):
    if number.isnumeric():
        return True
    else:
        return False


def check_admin_choice(number):
    if number == 1:
        passenger_settings_choice()
    elif number == 2:
        flight_settings_choice()


def print_passenger_panel():
    print("PASSENGER CONTROL: \n")
    print("1) Add Passenger")
    print("2) Get List of Passengers")


def passenger_settings_choice():
    print_passenger_panel()
    back_code = False
    while not back_code:
        user_choice = input(
            "Pick a number 1-2 to navigate the menu. type 'back' if you want to return to the Admin menu or 'exit' to logout \n")
        if user_choice == 'back':
            back_code = True
        elif user_choice == 'exit':
             exit_system()
        else:
            if check_if_number(user_choice):
                check_passenger_choice(int(user_choice))
                print_passenger_panel()


def check_passenger_choice(number):
    if number == 1:
        print(add_passenger())
    elif number == 2:
        print(get_all_passengers())


def check_for_back_passenger(user_input):
    if user_input == 'back':
        back_to_passenger()

def add_passenger():
    name = input("Enter name of the new Passenger \n")
    check_for_back_passenger(name)
    tax = input(f'Enter Tax No. for {name} \n')
    check_for_back_passenger(tax)
    passport = input(f'Enter Passport No. for {name} \n')
    check_for_back_passenger(passport)
    dob = input(f'Enter Date of Birth for {name} \n')
    check_for_back_passenger(dob)
    with_child = False
    correct_input = False
    while not correct_input:
        user_input = input(f'Does {name} have a child? (Y/N)')
        if user_input.upper() == "Y":
            with_child = True
            correct_input = True
        elif user_input.upper() == "N":
            correct_input = True
        else:
            "Incorrect Input"
    passenger_list.append(Passenger(name, tax, passport, dob, with_child))
    return f'{name} added'


def get_all_passengers():
    passenger_names = []
    for passenger in passenger_list:
        passenger_names.append(passenger.name)
    return passenger_names


def print_flight_panel():
    print("FLIGHT CONTROL: \n")
    print("1) Add Flight")
    print("2) Add Passenger to Flight")
    print("3) Remove Passenger From Flight")
    print("4) Get All Passengers in Flight")
    print("5) Get All Flights")
    print("6) Total Revenue!")


def flight_settings_choice():
    print_flight_panel()
    back_code = False
    while not back_code:
        user_choice = input(
            "Pick a number 1-6 to navigate the menu. type 'back' if you want to return to the Admin menu or 'exit' to logout\n")
        if user_choice == 'back':
            back_code = True
        elif user_choice == 'exit':
             exit_system()
        else:
            if check_if_number(user_choice):
                check_flight_choice(int(user_choice))
                print_flight_panel()


def check_flight_choice(number):
    if number == 1:
        print(add_flight())
    elif number == 2:
        print(add_passenger_to_flight())
    elif number == 3:
        print(remove_passenger_from_flight())
    elif number == 4:
        get_all_passengers_in_flight()
    elif number == 5:
        get_all_flights()
    elif number == 6:
        print(get_total_revenue())


def check_for_back_flight(user_input):
    if user_input == 'back':
        back_to_flight()


def add_flight():
    input_correct = False
    flight_no = ''
    seats = ''
    while not input_correct:
        user_input = input("Enter Flight Number:\n")
        if check_if_number(user_input):
            flight_no = int(user_input)
            input_correct = True
        else:
            print("Invalid Input")
    destination = input("Please enter Destination: \n")
    check_for_back_flight(destination)
    date = input("Enter flight date: \n")
    check_for_back_flight(date)
    time = input("Enter flight time: \n")
    check_for_back_flight(time)
    input_correct = False
    while not input_correct:
        user_input = input("Enter number of seats")
        if check_if_number(user_input):
            seats = int(user_input)
            input_correct = True
        else:
            print("Invalid Input")
    flight_list.append(FlightTrip(flight_no, destination, date, time, seats, seats))
    return f'Flight to {destination} added!'


def add_passenger_to_flight():
    selected_flight = ''
    flight_num = False
    for x in range(1, len(flight_list) + 1):
        if flight_list[x - 1].available_seats > 0:
            print(
                f'{x}) Flying to {flight_list[x - 1].destination} on {flight_list[x - 1].flight_date}\n')
        else:
            return "All flights already full!"
    while not flight_num:
        user_choice = input("Pick a Flight to add Passenger to using the number guide \n")
        if check_if_number(user_choice):
            if int(user_choice) <= len(flight_list):
                selected_flight = flight_list[int(user_choice) - 1]
                flight_num = True
            else:
                print("Invalid number selected")
        else:
            print("Invalid number selected")
    passenger_num = False
    result = False
    for x in range(1, len(passenger_list) + 1):
        if passenger_list[x - 1] not in selected_flight.return_passenger_list():
            print(f'{x}) {passenger_list[x - 1].name} (Passport No: {passenger_list[x - 1].passport_no})\n')
            result = True
    if not result:
        return "All passengers already on board this flight"
    while not passenger_num:
        user_choice = input("Pick a Passenger to add using the number guide \n")
        if check_if_number(user_choice):
            if int(user_choice) <= len(passenger_list):
                selected_flight.add_passenger(passenger_list[int(user_choice) - 1])
                passenger_num = True
                return f'{passenger_list[int(user_choice) - 1].name} added to flight!'
            else:
                print("Invalid number selected")
        else:
            print("Invalid number selected")


def remove_passenger_from_flight():
    selected_flight = ''
    flight_num = False
    for x in range(1, len(flight_list) + 1):
        if flight_list[x - 1].available_seats < flight_list[x - 1].seats:
            print(
                f'{x}) Flying to {flight_list[x - 1].destination} on {flight_list[x - 1].flight_date}\n')
        else:
            return "All flights already empty!"
    while not flight_num:
        user_choice = input("Pick a Flight to remove Passenger from using the number guide \n")
        if check_if_number(user_choice):
            if int(user_choice) <= len(flight_list):
                selected_flight = flight_list[int(user_choice) - 1]
                flight_num = True
            else:
                print("Invalid number selected")
        else:
            print("Invalid number selected")
    passenger_num = False
    if len(selected_flight.return_passenger_list()) == 0:
        return "Flight is Empty!"
    else:
        for x in range(1, len(selected_flight.return_passenger_list()) + 1):
            print(f'{x}) {selected_flight.return_passenger_list()[x - 1].name} (Passport No: {selected_flight.return_passenger_list()[x - 1].passport_no})\n')

    while not passenger_num:
        user_choice = input("Pick a Passenger to remove using the number guide \n")
        if check_if_number(user_choice):
            if int(user_choice) <= len(selected_flight.return_passenger_list()):
                removed_passenger = selected_flight.return_passenger_list()[int(user_choice) - 1]
                selected_flight.remove_passenger(removed_passenger.passport_no)
                passenger_num = True
                return f'{removed_passenger.name} removed from flight!'
            else:
                print("Invalid number selected")
        else:
            print("Invalid number selected")


def get_all_passengers_in_flight():
    selected_flight = ''
    flight_num = False
    for x in range(1, len(flight_list) + 1):
        print(flight_list[x - 1].available_seats)
        print(flight_list[x - 1].seats)

        if flight_list[x - 1].available_seats < flight_list[x - 1].seats:
            print(f'{x}) Flying to {flight_list[x - 1].destination} on {flight_list[x - 1].flight_date}\n')
        else:
            return "All flights already empty!"
    while not flight_num:
        user_choice = input("Pick a Flight to get all Passengers from using the number guide \n")
        if check_if_number(user_choice):
            if int(user_choice) <= len(flight_list):
                selected_flight = flight_list[int(user_choice) - 1]
                flight_num = True
            else:
                print("Invalid number selected")
        else:
            print("Invalid number selected")
    selected_flight.flight_attendee_report()


def get_all_flights():
    if len(flight_list) > 0:
        for x in range(1, len(flight_list) + 1):
            print(f'{x}) Flying to {flight_list[x - 1].destination} on {flight_list[x - 1].flight_date}\n')
    else:
        return "No available flights"


def get_total_revenue():
    total_profit = 0
    if len(flight_list) > 0:
        for x in range(1, len(flight_list) + 1):
            total_profit += flight_list[x-1].ticket_revenue()
    return f'Total Money made so far is £{total_profit}'