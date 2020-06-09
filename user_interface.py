from phsh import *
from ui_functions import *
import time

print('WELCOME!')
time.sleep(1)
print('As our new admin, you will be in charge of managing the flights and passengers in our system. \n')
time.sleep(0.5)
print("Your password will be 'group1flight' to log in.")

pword_verified = False
while not pword_verified:
    user_access_attempt = input("Please Enter Password: \n")
    if verify_password(user_access_attempt):
        print("Password Accepted")
        pword_verified = True
    else:
        print("Password Incorrect")
print("Welcome! What would you like to do first? \n")
print_panel()
exit_code = False
while not exit_code:
    user_choice = input("Pick a number 1 or 2 to navigate the menu. type 'exit' when you want to log out \n")
    if user_choice == 'exit':
        exit_code = True
    else:
        if check_if_number(user_choice):
            check_admin_choice(int(user_choice))
            print_panel()
print("Logout Successful")
