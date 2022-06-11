def calculate_factorial(number):
    for factorial in range(1, number):
        number *= factorial
    return number


num_1 = int(input())
num_2 = int(input())
first_number_factorial = calculate_factorial(num_1)
second_number_factorial = calculate_factorial(num_2)
result = first_number_factorial / second_number_factorial
print(f'{result:.2f}')
