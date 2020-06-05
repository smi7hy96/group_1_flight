class Plane:
    def __init__(self, model, __seats, __adult_price, __child_price, __infant_price):
        self.model = model
        self.__seats = __seats
        self.__adult_price = __adult_price
        self.__child_price = __child_price
        self.__infant_price = __infant_price

    def get_adult_price(self):
        return self.__adult_price

    def get_child_price(self):
        return self.__child_price

    def get_infant_price(self):
        return self.__infant_price

    def get_seats(self):
        return self.__seats

