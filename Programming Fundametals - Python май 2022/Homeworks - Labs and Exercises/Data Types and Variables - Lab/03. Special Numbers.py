n = int(input())

for i in range(1, n + 1):
    sum_digits = 0
    digits = i
    while digits > 0:
        sum_digits += digits % 10
        digits = int(digits / 10)

    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')
