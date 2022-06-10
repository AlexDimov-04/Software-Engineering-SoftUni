factor = int(input())
count = int(input())
list_nums = []

for multiplier in range(1, count + 1):
    list_nums.append(factor * multiplier)
print(list_nums)