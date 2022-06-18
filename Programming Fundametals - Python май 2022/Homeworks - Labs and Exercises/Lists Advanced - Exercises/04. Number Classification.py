def positive_numbers(numbers):
    return [num for num in numbers if int(num) >= 0]


def negative_numbers(numbers):
    return [num for num in numbers if int(num) < 0]


def even_numbers(numbers):
    return [num for num in numbers if int(num) % 2 == 0]


def odd_numbers(numbers):
    return [num for num in numbers if int(num) % 2 != 0]


numbers_as_strings = input().split(', ')

print(f"Positive: {', '.join(positive_numbers(numbers_as_strings))}")
print(f"Negative: {', '.join(negative_numbers(numbers_as_strings))}")
print(f"Even: {', '.join(even_numbers(numbers_as_strings))}")
print(f"Odd: {', '.join(odd_numbers(numbers_as_strings))}")