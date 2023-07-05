numbers = list(map(int, input().split()))

# recursive method
def sum_arr_recursively(arr, idx):
    if idx == len(arr) - 1:
        return arr[idx]
    return arr[idx] + sum_arr_recursively(arr, idx + 1)

print(sum_arr_recursively(numbers, 0))

# iterative method (time preferable)
"""
total_sum = 0
for n in numbers:
    total_sum += n
print(total_sum)
"""

# easiest built-in method
# print(sum(numbers))
