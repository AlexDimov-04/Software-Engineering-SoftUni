from unittest import main, TestCase
from project.bookstore import Bookstore


class TestBookstore(TestCase):
    def setUp(self):
        self.bookstore = Bookstore(500)

    def test_correct_books_initialization(self):
        self.assertEqual(self.bookstore.books_limit, 500)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {})
        self.assertEqual(self.bookstore.total_sold_books, 0)

    def test_books_limit_raise_value_error_if_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0

        self.assertEqual(str(ve.exception), f"Books limit of 0 is not valid")

    def test_count_total_books_in_the_bookstore(self):
        self.bookstore.availability_in_store_by_book_titles = {
            'Harry Potter': 10,
            'Lord of the Rings': 50,
            'The Godfather': 20
        }

        self.assertEqual(len(self.bookstore), 80)

    def test_receive_book_with_over_the_reached_limit_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book('Harry Potter', 550)

        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")

    def test_receive_a_new_book_and_set_it_in_the_bookstore(self):
        self.bookstore.availability_in_store_by_book_titles = {'Harry Potter': 10}
        result = self.bookstore.receive_book('Top Gun', 7)

        self.assertEqual(result, "7 copies of Top Gun are available in the bookstore.")

    def test_receive_a_count_for_a_existing_book(self):
        self.bookstore.availability_in_store_by_book_titles = {'Harry Potter': 10}
        result = self.bookstore.receive_book('Harry Potter', 7)

        self.assertEqual("17 copies of Harry Potter are available in the bookstore.", result)

    def test_to_sell_book_if_the_book_is_not_available_in_the_bookstore_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('The Fault in our stars', 40)

        self.assertEqual(str(ex.exception), "Book The Fault in our stars doesn't exist!")

    def test_to_sell_book_if_there_is_not_enough_copies_of_that_book_raise_exception(self):
        self.bookstore.availability_in_store_by_book_titles = {'The Fault in our stars': 50}

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('The Fault in our stars', 60)

        self.assertEqual(str(ex.exception),
                         "The Fault in our stars has not enough copies to sell. "
                         "Left: 50")

    def test_to_sell_book_if_everything_is_available(self):
        self.bookstore.availability_in_store_by_book_titles = {'Scarface': 20, 'Book': 4}
        result = self.bookstore.sell_book('Scarface', 20)

        self.assertEqual(len(self.bookstore.availability_in_store_by_book_titles), 2)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles['Scarface'], 0)
        self.assertEqual(self.bookstore.total_sold_books, 20)
        self.assertEqual(result, "Sold 20 copies of Scarface")

    def test_correct__str__formatting(self):
        self.bookstore.availability_in_store_by_book_titles = {'Scarface': 20, 'Book': 4}

        self.assertEqual(str(self.bookstore),
                         "Total sold books: 0\n"
                         "Current availability: 24\n"
                         " - Scarface: 20 copies\n"
                         " - Book: 4 copies")


if __name__ == '__main__':
    main()
