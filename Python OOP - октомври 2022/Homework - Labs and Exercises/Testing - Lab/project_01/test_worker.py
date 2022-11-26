from unittest import TestCase, main
from project_01.worker import Worker


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker('Alex', 1000, 100)

    def test_correct_initializing(self):
        self.assertEqual(self.worker.name, 'Alex')
        self.assertEqual(self.worker.salary, 1000)
        self.assertEqual(self.worker.energy, 100)
        self.assertEqual(self.worker.money, 0)

    def test_increment_money_for_worker_if_working(self):
        self.worker.work()
        self.assertEqual(self.worker.money, 1000)

    def test_decrease_money_for_worker_if_working(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 99)

    def test_raise_exception_whether_worker_has_zero_or_negative_energy(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_increase_energy_after_rest(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 101)

    def test_get_correct_information(self):
        self.assertEqual('Alex has saved 0 money.', self.worker.get_info())


if __name__ == '__main__':
    main()
