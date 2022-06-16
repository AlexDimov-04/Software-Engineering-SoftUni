def is_perfect(number):
    sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum += divisor
    if number == sum:
        return "We have a perfect number!"
    else:
        return "It's not so perfect"


number = int(input())
print(is_perfect(number))
