from unittest import main, TestCase
from project.library import Library


class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library('Ciela')
        self.library.books_by_authors = {'John Smith': ['Die Harder'],
                                         'Aaron Paul': ['Breaking Bad']}
        self.library.readers = {'Alex': [], 'Dimo': []}

    def test_correct_initialization(self):
        self.assertEqual(self.library.name, 'Ciela')
        self.assertEqual(self.library.books_by_authors, {'John Smith': ['Die Harder'],
                                                         'Aaron Paul': ['Breaking Bad']})
        self.assertEqual(self.library.readers, {'Alex': [], 'Dimo': []})

    def test_an_empty_string_name_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ''

        self.assertEqual(str(ve.exception), "Name cannot be empty string!")

    def test_add_a_new_title_to_the_author_books_by_authors_dict(self):
        self.library.add_book('Aaron Paul', 'Shining')
        self.assertEqual(self.library.books_by_authors, {'John Smith': ['Die Harder'],
                                                         'Aaron Paul': ['Breaking Bad', 'Shining']})

    def test_add_a_new_author_to_the_author_books_by_authors_dict(self):
        self.library.add_book('Chuck Norris', 'Crocodile')
        self.assertEqual(self.library.books_by_authors, {'John Smith': ['Die Harder'],
                                                         'Aaron Paul': ['Breaking Bad'],
                                                         'Chuck Norris': ['Crocodile']})

    def test_to_add_a_new_reader_to_the_library_readers(self):
        self.library.add_reader('Tanq')
        self.assertEqual(self.library.readers, {'Alex': [], 'Dimo': [], 'Tanq': []})

    def test_to_add_a_reader_who_is_already_registered_in_the_library(self):
        result = self.library.add_reader('Alex')

        self.assertEqual(self.library.readers, {'Alex': [], 'Dimo': []})
        self.assertEqual(result, "Alex is already registered in the Ciela library.")

    def test_to_rent_a_book_if_the_reader_not_in_the_library_readers(self):
        result = self.library.rent_book('Gosho', 'John Smith', 'Die Harder')
        self.assertEqual(result, "Gosho is not registered in the Ciela Library.")

    def test_to_rent_a_book_if_the_book_author_is_not_in_the_book_by_authors_dict(self):
        result = self.library.rent_book('Alex', 'Andrew Lincoln', 'The Walking Dead')
        self.assertEqual(result, "Ciela Library does not have any Andrew Lincoln's books.")

    def test_to_rent_a_book_if_the_book_title_is_not_in_the_book_by_authors_dict_values(self):
        result = self.library.rent_book('Alex', 'John Smith', 'The Bomb')
        self.assertEqual(result, "Ciela Library does not have John Smith's \"The Bomb\".")

    def test_to_rent_a_new_book_from_the_library(self):
        self.library.rent_book('Alex', 'John Smith', 'Die Harder')

        self.assertEqual(self.library.readers, {'Alex': [{"John Smith": 'Die Harder'}], 'Dimo': []})
        self.assertEqual(self.library.books_by_authors, {'Aaron Paul': ['Breaking Bad'], 'John Smith': []})


if __name__ == '__main__':
    main()
