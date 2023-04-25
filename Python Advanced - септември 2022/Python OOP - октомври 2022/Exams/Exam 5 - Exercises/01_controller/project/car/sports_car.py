from project.car.car import Car


class SportsCar(Car):
    MIN_SPEED = 400
    MAX_SPEED = 600

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if not SportsCar.MIN_SPEED <= value <= SportsCar.MAX_SPEED:
            raise ValueError(f"Invalid speed limit! Must be between {SportsCar.MIN_SPEED} and {SportsCar.MAX_SPEED}!")

        self.__speed_limit = value
