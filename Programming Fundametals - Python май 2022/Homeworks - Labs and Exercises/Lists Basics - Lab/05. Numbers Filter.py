n = int(input())

numbers = []
filtered_nums = []

for i in range(n):
    num = int(input())
    numbers.append(num)

command = input()

for j in numbers:
    filter_command = (
        (command == 'even' and j % 2 == 0) or
        (command == 'odd' and j % 2 != 0) or
        (command == 'negative' and j < 0) or
        (command == 'positive' and j >= 0)
    )

    if filter_command:
        filtered_nums.append(j)

print(filtered_nums)
