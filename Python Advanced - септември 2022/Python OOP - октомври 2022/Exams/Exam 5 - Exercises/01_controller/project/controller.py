from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    CAR_TYPES = {'MuscleCar': MuscleCar,
                 'SportsCar': SportsCar}

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def __find_car(self, type_car: str):
        try:
            return [c for c in self.cars if c.__class__.__name__ == type_car and not c.is_taken][-1]
        except IndexError:
            return None

    def __find_driver(self, driver_name: str):
        for d in self.drivers:
            if d.name == driver_name:
                return d

    def __find_race(self, race_name: str):
        for r in self.races:
            if r.name == race_name:
                return r

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if [car for car in self.cars if car.model == model]:
            raise Exception(f"Car {model} is already created!")

        if car_type in Controller.CAR_TYPES:
            car = Controller.CAR_TYPES[car_type](model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if [driver for driver in self.drivers if driver.name == driver_name]:
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if [race for race in self.races if race.name == race_name]:
            raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver(driver_name)
        new_car = self.__find_car(car_type)

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if all(c.is_taken and new_car for c in self.cars) or not new_car:
            raise Exception(f"Car {car_type} could not be found!")

        if any(not c.is_taken for c in self.cars) and driver.car is not None:
            old_car_model = driver.car.model
            driver.car.is_taken = False

            driver.car = new_car
            new_car.is_taken = True

            return f"Driver {driver_name} changed his car from {old_car_model} to {new_car.model}."

        if driver.car is None and not new_car.is_taken:
            driver.car = new_car
            new_car.is_taken = True

            return f"Driver {driver_name} chose the car {new_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        driver = self.__find_driver(driver_name)
        race = self.__find_race(race_name)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        if race and driver and driver.car is not None:
            race.drivers.append(driver)
            return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_race(race_name)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        output = []
        for driver in sorted(race.drivers, key=lambda x: -x.car.speed_limit)[:3]:
            driver.number_of_wins += 1

            if len(output) < 3:
                output.append(f"Driver {driver.name} wins the {race_name} race with a speed of "
                              f"{driver.car.speed_limit}.")

        return '\n'.join(output)
