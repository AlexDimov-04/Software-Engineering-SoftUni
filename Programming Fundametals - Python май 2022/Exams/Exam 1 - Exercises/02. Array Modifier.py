numbers = [int(x) for x in input().split(' ')]

while True:
    command = input().split(' ')

    if command[0] == 'end':
        break

    if command[0] == 'swap':
        index_1 = int(command[1])
        index_2 = int(command[2])
        numbers[index_1], numbers[index_2] = numbers[index_2], numbers[index_1]
    elif command[0] == 'multiply':
        index_1 = int(command[1])
        index_2 = int(command[2])
        multiplied = numbers[index_1] * numbers[index_2]
        numbers.pop(index_1)
        numbers.insert(index_1, multiplied)
    elif command[0] == 'decrease':
        numbers = [x - 1 for x in numbers]

print(', '.join(map(str, numbers)))
