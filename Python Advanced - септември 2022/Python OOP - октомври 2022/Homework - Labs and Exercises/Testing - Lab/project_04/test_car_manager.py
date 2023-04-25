from unittest import TestCase, main
from project_04.car_manager import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car('Citroen', 'C4', 7, 100)

    def test_correct_initializing(self):
        self.assertEqual(self.car.make, 'Citroen')
        self.assertEqual(self.car.model, 'C4')
        self.assertEqual(self.car.fuel_consumption, 7)
        self.assertEqual(self.car.fuel_capacity, 100)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_no_make_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_model_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_zero_fuel_consumption_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_zero_fuel_capacity_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_zero_fuel_amount_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def test_refuel_with_zero_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_with_more_fuel_than_capacity_expect_full_tank(self):
        self.car.refuel(150)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_drive_without_more_than_possible_raise_exception(self):
        self.car.fuel_amount = 20

        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)

        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")

    def test_drive_valid_distance_expect_fuel_amount_reduce(self):
        self.car.fuel_amount = 75
        self.car.drive(100)

        self.assertEqual(self.car.fuel_amount, 68)


if __name__ == '__main__':
    main()
