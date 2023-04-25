from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal('Daryl', 'dog', 'woof')

    def test_correct_initializing(self):
        self.assertEqual(self.mammal.name, 'Daryl')
        self.assertEqual(self.mammal.type, 'dog')
        self.assertEqual(self.mammal.sound, 'woof')
        self.assertEqual(self.mammal._Mammal__kingdom, 'animals')

    def test_the_sound_of_the_animal_based_on_their_type(self):
        result = self.mammal.make_sound()
        self.assertEqual(result, "Daryl makes woof")

    def test_the_kingdom_of_the_animal_based_on_their_type(self):
        result = self.mammal.get_kingdom()
        self.assertEqual(result, "animals")

    def test_info_for_the_particular_animal_type(self):
        result = self.mammal.info()
        self.assertEqual(result, 'Daryl is of type dog')


if __name__ == '__main__':
    main()
