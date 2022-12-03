from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    SPEED_ADD = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed = self.MAX_SPEED if self.speed + Appaloosa.SPEED_ADD > Appaloosa.MAX_SPEED else self.speed + \
                                                                                                   Appaloosa.SPEED_ADD
