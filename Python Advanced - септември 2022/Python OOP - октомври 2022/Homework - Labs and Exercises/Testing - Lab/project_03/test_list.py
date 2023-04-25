from unittest import TestCase, main
from project_03.list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.integer_list = IntegerList('50', 1, False, 3.5, 2, 3)

    def test_correct_initializing(self):
        self.assertEqual(self.integer_list._IntegerList__data, [1, 2, 3])

    def test_correct_get_data(self):
        self.assertEqual(self.integer_list.get_data(), [1, 2, 3])

    def test_add_with_non_integer_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add('string')

        self.assertEqual(str(ve.exception), "Element is not Integer")

    def test_add_correct(self):
        result = self.integer_list.add(4)

        self.assertEqual(result, [1, 2, 3, 4])
        self.assertEqual(self.integer_list._IntegerList__data, [1, 2, 3, 4])

    def test_remove_index_with_invalid_index_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(3)

        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_remove_index_with_correct_index(self):
        result = self.integer_list.remove_index(1)

        self.assertNotIn(2, self.integer_list._IntegerList__data)
        self.assertEqual(result, 2)

    def test_get_invalid_index_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(3)

        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_valid_index(self):
        self.assertEqual(self.integer_list.get(1), 2)

    def test_insert_with_invalid_index_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(3, 4)

        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_insert_with_non_integer_element_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(2, '4')

        self.assertEqual(str(ve.exception), "Element is not Integer")

    def test_insert_correct(self):
        self.integer_list.insert(2, 4)
        self.assertEqual(self.integer_list._IntegerList__data, [1, 2, 4, 3])

    def test_get_biggest_number(self):
        self.assertEqual(self.integer_list.get_biggest(), 3)

    def test_get_correct_index(self):
        self.assertEqual(self.integer_list.get_index(1), 0)


if __name__ == "__main__":
    main()
