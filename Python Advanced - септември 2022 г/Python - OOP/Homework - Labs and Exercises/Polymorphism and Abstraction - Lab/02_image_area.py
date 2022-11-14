class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __gt__(self, value):
        return self.get_area() > value.get_area()

    def __ge__(self, value):
        return self.get_area() >= value.get_area()

    def __lt__(self, value):
        return self.get_area() < value.get_area()

    def __le__(self, value):
        return self.get_area() <= value.get_area()

    def __eq__(self, value):
        return self.get_area() == value.get_area()

    def __ne__(self, value):
        return self.get_area() != value.get_area()


a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a1)
print(a1 != a3)
