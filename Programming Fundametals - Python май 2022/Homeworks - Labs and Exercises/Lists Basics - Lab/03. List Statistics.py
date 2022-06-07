n = int(input())

positive_count = 0
positive_nums = []
negative_nums = []

for i in range(n):
    num = int(input())

    if num >= 0:
        positive_nums.append(num)
        positive_count += 1
    else:
        negative_nums.append(num)

print(positive_nums)
print(negative_nums)
print(f'Count of positives: {positive_count}')
print(f'Sum of negatives: {sum(negative_nums)}')
