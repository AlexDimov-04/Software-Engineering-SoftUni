def sum_numbers(first, second):
    return first + second


def subtract(sum, third):
    return sum - third


def add_and_subtract(first, second, third):
    num_1_num_2_sum = sum_numbers(first, second)
    result = subtract(num_1_num_2_sum, third)
    return result


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(add_and_subtract(num_1, num_2, num_3))
