n = int(input())

# recursive method
def fact(num):
    if num <= 1:
        return 1
    return num * fact(num - 1)

print(fact(n))

# iterative method
"""
total_sum = 1
for i in range(1, n + 1):
    total_sum *= i
print(total_sum)
"""

