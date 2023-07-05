from functools import lru_cache

n = int(input())

# recursive method
@lru_cache()
def fib(num):
    if num <= 1:
        return 1
    return fib(num - 1) + fib(num - 2)

print(fib(n))

# iterative method

"""
def iterative_fib(num):
    fib0, fib1 = 1, 1

    for _ in range(num - 1):
        result = fib0 + fib1
        fib0, fib1 = fib1, result
    return result

print(iterative_fib(n))
"""