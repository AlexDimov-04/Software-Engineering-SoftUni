def sum_even_odd_digits(n):
    even = 0
    odd = 0
    nums = []
    for digits in n:
        nums.append(digits)
    integer_nums = list(map(int, nums))
    for number in integer_nums:
        if number % 2 == 0:
            even += number
        elif number % 2 != 0:
            odd += number

    return f'Odd sum = {odd}, Even sum = {even}'


n = input()
print(sum_even_odd_digits(n))


