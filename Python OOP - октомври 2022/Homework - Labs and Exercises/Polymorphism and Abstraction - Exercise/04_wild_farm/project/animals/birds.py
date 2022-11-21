from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Seed, Meat


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @property
    def gained_weight(self):
        return 0.35

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit, Seed, Meat]

    def make_sound(self):
        return "Cluck"
