from unittest import main, TestCase

from project.plantation import Plantation


class TestPlantation(TestCase):
    def setUp(self):
        self.plantation = Plantation(10)
        self.plantation.workers = ['Alex', 'Ivan', 'Drago']
        self.plantation.plants = {'Alex': ['Roses'], 'Drago': ['Tulips']}

    def test_correct_initialization(self):
        self.assertEqual(self.plantation.size, 10)
        self.assertEqual(self.plantation.plants, {'Alex': ['Roses'], 'Drago': ['Tulips']})
        self.assertEqual(self.plantation.workers, ['Alex', 'Ivan', 'Drago'])

    def test_size_invalid_number_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1

        self.assertEqual(str(ve.exception), "Size must be positive number!")

    def test_to_hire_worker_if_worker_is_already_hired_raise_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker('Alex')

        self.assertEqual(str(ve.exception), "Worker already hired!")

    def test_to_hire_worker_successfully_and_append_him_to_workers_list(self):
        result = self.plantation.hire_worker('Marin')

        self.assertEqual(len(self.plantation.workers), 4)
        self.assertEqual(result, f"Marin successfully hired.")

    def test__len__method_for_the_count_of_all_plants(self):
        self.assertEqual(len(self.plantation), 2)

    def test_to_check_to_plant_if_worker_is_not_hired_raise_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('Negan', 'Narcissus')

        self.assertEqual(str(ve.exception), "Worker with name Negan is not hired!")

    def test_to_check_if_length_of_the_plantation_is_bigger_than_the_size_raise_exception(self):
        self.plantation.plants = {'Alex': 'Roses', 'Drago': 'Tulips'}

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('Alex', 'Dahlias')

        self.assertEqual(str(ve.exception), "The plantation is full!")

    def test_to_check_if_worker_is_in_plants_dict_append_plant(self):
        result = self.plantation.planting('Drago', 'Cauliflower')

        self.assertEqual(len(self.plantation.plants['Drago']), 2)
        self.assertEqual(result, "Drago planted Cauliflower.")

    def test_to_add_a_new_worker_with_a_new_plant_to_plants_dict(self):
        result = self.plantation.planting('Ivan', 'plant_name')

        self.assertEqual(self.plantation.plants, {'Alex': ['Roses'], 'Drago': ['Tulips'], 'Ivan': ['plant_name']})
        self.assertEqual(result, "Ivan planted it's first plant_name.")

    def test_correct__str__result(self):
        self.plantation.workers = ['Stoqn', 'Ivan']
        self.plantation.plants = {'Alex': ['Roses']}

        self.assertEqual(str(self.plantation),
                         f"Plantation size: 10\n"
                         f"Stoqn, Ivan\n"
                         f"Alex planted: Roses")

    def test_correct__repr__result(self):
        self.assertEqual(repr(self.plantation),
                         f"Size: 10\n"
                         f"Workers: Alex, Ivan, Drago")


if __name__ == "__main__":
    main()
