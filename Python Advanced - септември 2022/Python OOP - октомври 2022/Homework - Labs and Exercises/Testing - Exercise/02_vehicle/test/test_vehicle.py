from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(20.5, 175.5)

    def test_default_fuel_consumption_correct(self):
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def test_correct_initializing(self):
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(self.vehicle.fuel, 20.5)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(self.vehicle.horse_power, 175.5)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_car_without_enough_fuel(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_drive_car_with_enough_fuel_expect_fuel_decrease(self):
        self.vehicle.drive(2)
        self.assertEqual(self.vehicle.fuel, 18)

    def test_refuel_full_car_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)

        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_refuel_car_with_needed_fuel(self):
        self.vehicle.refuel(0)
        self.assertEqual(self.vehicle.fuel, 20.5)

    def test_correct__str__(self):
        result = str(self.vehicle)
        expected_result = f"The vehicle has {self.vehicle.horse_power} " \
                          f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} " \
                          f"fuel consumption"

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    main()
