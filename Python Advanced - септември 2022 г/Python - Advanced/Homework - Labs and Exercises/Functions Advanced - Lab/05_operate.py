from functools import reduce


def operate(operator, *args):
    if operator == '+':
        return sum(args)
    elif operator == '-':
        result = reduce(lambda x, y: x - y, args)
        return result
    elif operator == '*':
        result = reduce(lambda x, y: x * y, args)
        return result
    elif operator == '/':
        result = reduce(lambda x, y: x / y, args)
        return result
