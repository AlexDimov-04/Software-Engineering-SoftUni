from unittest import main, TestCase
from project.toy_store import ToyStore


class TestToyStore(TestCase):
    def setUp(self):
        self.toy_shelf = ToyStore()

    def test_correct_initialization(self):
        self.assertEqual(self.toy_shelf.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_to_add_a_toy_to_a_shelf_that_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy_shelf.add_toy('H', 'Puppet')

        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_to_add_a_toy_that_is_already_in_the_shelf(self):
        self.toy_shelf.toy_shelf['A'] = 'Puppet'

        with self.assertRaises(Exception) as ex:
            self.toy_shelf.add_toy('A', 'Puppet')

        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_to_add_a_toy_to_an_already_taken_shelf(self):
        self.toy_shelf.toy_shelf['A'] = 'Robot'

        with self.assertRaises(Exception) as ex:
            self.toy_shelf.add_toy('A', 'Car')

        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_to_add_a_toy_successfully(self):
        result = self.toy_shelf.add_toy('B', 'Coala')
        self.assertEqual(self.toy_shelf.toy_shelf, {
            "A": None,
            "B": 'Coala',
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })
        self.assertEqual(result, "Toy:Coala placed successfully!")

    def test_to_remove_a_toy_from_non_existing_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy_shelf.remove_toy('Z', 'igrachka')

        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_to_remove_an_already_existing_toy(self):
        with self.assertRaises(Exception) as ex:
            self.toy_shelf.remove_toy('A', 'igrachka1')

        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_to_remove_a_toy_successfully(self):
        self.toy_shelf.toy_shelf['C'] = 'Mouse'

        result = self.toy_shelf.remove_toy('C', 'Mouse')
        self.assertEqual(self.toy_shelf.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })
        self.assertEqual(result, "Remove toy:Mouse successfully!")


if __name__ == "__main__":
    main()
