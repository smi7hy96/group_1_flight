from people import People


class Passenger(People):
    def __init__(self, name, tax_no, adult, passport_no, d_o_b):
        super().__init__(name, tax_no, adult)
        self._passport_no = passport_no
        self._d_o_b = d_o_b
        self.passenger_price = None
        self.set_ticket_price()

    def set_ticket_price(self):
        if self.adult:
            self.passenger_price = 10
        else:
            self.passenger_price = 5
