from functools import reduce


class Calculator:
    @staticmethod
    def add(*args):
        args = reduce(lambda x, y: x + y, args)
        return args

    @staticmethod
    def multiply(*args):
        args = reduce(lambda x, y: x * y, args)
        return args

    @staticmethod
    def divide(*args):
        args = reduce(lambda x, y: x / y, args)
        return args

    @staticmethod
    def subtract(*args):
        args = reduce(lambda x, y: x - y, args)
        return args


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
