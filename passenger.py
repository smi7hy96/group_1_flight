from people import People


class Passenger(People):
    def __init__(self, name, tax_no, passport_no, d_o_b, with_child=False):
        super().__init__(name, tax_no)
        self.__passport_no = passport_no
        self.__d_o_b = d_o_b
        self.passenger_price = None
        self.with_child = with_child
        self.child_name = None
        self.__child_passport_no = None
        self.__child_dob = None
        self.set_ticket_price()
        self.infant_passport()
        self.infant_name()
        self.infant_dob()

    def set_ticket_price(self):
        if self.with_child:
            self.passenger_price = 15
        else:
            self.passenger_price = 10

    def infant_passport(self):
        if self.with_child:
            self.__child_passport_no = input(f"Welcome {self.name}, please enter your child's passport number. ")

    def infant_dob(self):
        if self.with_child:
            self.__child_dob = input("Please enter your child's Date of Birth. ")

    def infant_name(self):
        if self.with_child:
            self.child_name = input("Please enter your child's name. ")

    def get_passport_no(self):
        return self.__passport_no

    def get_dob(self):
        return self.__d_o_b

    def get_infant_pass_no(self):
        return self.__child_passport_no

    def get_infant_dob(self):
        return self.__child_dob

