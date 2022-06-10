def caculation(number_a, number_b, operation):
    if operation == 'multiply':
        return number_a * number_b
    elif operation == 'divide':
        return int(number_a / number_b)
    elif operation == 'add':
        return number_a + number_b
    elif operation == 'subtract':
        return number_a - number_b


type_of_operation = input()
first_num = int(input())
second_num = int(input())
print(caculation(first_num, second_num, type_of_operation))
