numbers = input().split(' ')
numbers_to_remove = int(input())
nums = []

for i in numbers:
    nums.append(int(i))
for remove in range(numbers_to_remove):
    min_number = min(nums)
    nums.remove(min_number)
print(', '.join(str(j) for j in nums))
