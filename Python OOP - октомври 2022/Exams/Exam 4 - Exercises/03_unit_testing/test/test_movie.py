from unittest import main, TestCase

from project.movie import Movie


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie('The Joker', 2010, 9.8)
        self.movie.actors = ['Heath Ledger', 'Bryan Cranston']
        self.other_movie = Movie('Batman', 2012, 9.5)

    def test_correct_initialization(self):
        self.assertEqual(self.movie.name, 'The Joker')
        self.assertEqual(self.movie.year, 2010)
        self.assertEqual(self.movie.rating, 9.8)
        self.assertEqual(self.movie.actors, ['Heath Ledger', 'Bryan Cranston'])

    def test_incorrect_name_initialized(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''

        self.assertEqual(str(ve.exception), "Name cannot be an empty string!")

    def test_incorrect_year_initialized(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886

        self.assertEqual(str(ve.exception), "Year is not valid!")

    def test_add_actor_if_it_is_not_in_the_actors_list(self):
        self.movie.add_actor('Brad Pitt')

        self.assertEqual(self.movie.actors, ['Heath Ledger', 'Bryan Cranston', 'Brad Pitt'])

    def test_to_add_actor_who_is_already_in_the_actors_list_return_message(self):
        result = self.movie.add_actor('Heath Ledger')

        self.assertEqual(result, "Heath Ledger is already added in the list of actors!")

    def test_to_compare_our_rating_with_other_movie_rating_return_message_if_our_movie_is_better(self):
        result = self.movie.__gt__(self.other_movie)
        self.assertEqual(result, '"The Joker" is better than "Batman"')

    def test_to_compare_our_rating_with_other_movie_rating_return_message_if_other_movie_is_better(self):
        self.other_movie.rating = 9.9
        result = self.movie.__gt__(self.other_movie)

        self.assertEqual(result, '"Batman" is better than "The Joker"')

    def test_correct__repr__method(self):
        repr_result = f"Name: The Joker\n" \
                      f"Year of Release: 2010\n" \
                      f"Rating: 9.80\n" \
                      f"Cast: Heath Ledger, Bryan Cranston"

        self.assertEqual(repr(self.movie), repr_result)


if __name__ == '__main__':
    main()
