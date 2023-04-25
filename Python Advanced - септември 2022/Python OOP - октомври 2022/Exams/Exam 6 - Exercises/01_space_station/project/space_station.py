from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_ASTRONAUT_TYPES = {
        'Biologist': Biologist,
        'Geodesist': Geodesist,
        'Meteorologist': Meteorologist
    }
    FAILED_MISSIONS = 0
    SUCCESSFUL_MISSIONS = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if [a for a in self.astronaut_repository.astronauts if a.name == name]:
            return f"{name} is already added."

        if astronaut_type in SpaceStation.VALID_ASTRONAUT_TYPES:
            astronaut = SpaceStation.VALID_ASTRONAUT_TYPES[astronaut_type](name)
            self.astronaut_repository.astronauts.append(astronaut)
            return f"Successfully added {astronaut_type}: {name}."
        else:
            raise Exception("Astronaut type is not valid!")

    def add_planet(self, name: str, items: str):
        if [p for p in self.planet_repository.planets if p.name == name]:
            return f"{name} is already added."

        planet = Planet(name)
        planet.items += items.split(', ')
        self.planet_repository.planets.append(planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        try:
            astronaut = next(filter(lambda a: a.name == name, self.astronaut_repository.astronauts))
            self.astronaut_repository.astronauts.remove(astronaut)
            return f"Astronaut {name} was retired!"
        except StopIteration:
            raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        try:
            planet = next(filter(lambda p: p.name == planet_name, self.planet_repository.planets))
        except StopIteration:
            raise Exception("Invalid planet name!")

        if [a.oxygen <= 30 for a in self.astronaut_repository.astronauts]:
            raise Exception("You need at least one astronaut to explore the planet!")

        astronauts = [a for a in sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen)]
        top_5_astronauts = [a for a in astronauts if a.oxygen > 30][:5]

        for astronaut in top_5_astronauts:
            while planet.items and astronaut.oxygen > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()

        if planet.items:
            SpaceStation.FAILED_MISSIONS += 1
            return "Mission is not completed."
        else:
            SpaceStation.SUCCESSFUL_MISSIONS += 1
            return f"Planet: {planet_name} was explored. {len(top_5_astronauts)} " \
                   "astronauts participated in collecting items."

    def report(self):
        output = [f"{SpaceStation.SUCCESSFUL_MISSIONS} successful missions!",
                  f"{SpaceStation.FAILED_MISSIONS} missions were not completed!",
                  "Astronauts' info:"]

        for a in self.astronaut_repository.astronauts:
            output.append(f"Name: {a.name}")
            output.append(f"Oxygen: {a.oxygen}")

            if a.backpack:
                output.append(f"Backpack items: {', '.join(a.backpack)}")
            else:
                output.append(f"Backpack items: none")

        return '\n'.join(output)
