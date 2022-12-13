from project.booths.booth import Booth


class PrivateBooth(Booth):
    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        price = 3.50 * number_of_people
        self.price_for_reservation = price
        self.is_reserved = True
