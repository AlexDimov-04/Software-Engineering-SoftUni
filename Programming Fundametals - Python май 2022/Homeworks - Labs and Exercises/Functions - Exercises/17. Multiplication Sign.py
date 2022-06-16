def multiplication_sign(num_1, num_2, num_3):
    if num_1 == 0 or num_2 == 0 or num_3 == 0:
        return 'zero'
    elif (num_1 > 0 and num_2 > 0 and num_3 > 0) or (num_1 < 0 and num_2 < 0 and num_3 > 0) or (num_1 < 0 and num_2 > 0 and num_3 < 0) or (num_1 > 0 and num_2 < 0 and num_3 < 0):
        return 'positive'
    return 'negative'


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(multiplication_sign(first_num, second_num, third_num))