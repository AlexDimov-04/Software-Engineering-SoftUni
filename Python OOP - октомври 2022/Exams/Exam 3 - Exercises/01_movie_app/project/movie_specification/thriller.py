from project.movie_specification.movie import Movie
from project.user import User


class Thriller(Movie):
    AGE_RESTRICTION = 16

    def __init__(self, title: str, year: int, owner: User, age_restriction: int = 16):
        super().__init__(title, year, owner, age_restriction)

    def details(self):
        return f"Thriller - Title:{self.title}, Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < Thriller.AGE_RESTRICTION:
            raise ValueError(f"Thriller movies must be restricted for audience under {Thriller.AGE_RESTRICTION} years!")

        self.__age_restriction = value
