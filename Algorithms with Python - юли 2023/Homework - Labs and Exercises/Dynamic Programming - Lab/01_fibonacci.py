n = int(input())
calculated_values = {}

def fib(n):
    if n in calculated_values:
        return calculated_values[n]
    elif n <= 2:
        value = 1
    else:
        value = fib(n-1) + fib(n-2)

    calculated_values[n] = value
    return value

print(fib(n))
