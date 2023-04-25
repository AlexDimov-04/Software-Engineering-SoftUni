from project.movie_specification.movie import Movie
from project.user import User


class Action(Movie):
    AGE_RESTRICTION = 12

    def __init__(self, title: str, year: int, owner: User, age_restriction: int = 12):
        super().__init__(title, year, owner, age_restriction)

    def details(self):
        return f"Action - Title:{self.title}, Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < Action.AGE_RESTRICTION:
            raise ValueError(f"Action movies must be restricted for audience under {Action.AGE_RESTRICTION} years!")

        self.__age_restriction = value
