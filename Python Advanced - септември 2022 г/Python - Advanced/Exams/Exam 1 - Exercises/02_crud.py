matrix = [[x for x in input().split()] for _ in range(6)]
start_pos = [int(x) for x in input() if x.isdigit()]
row, col = start_pos[0], start_pos[1]


def movement(direction, pos_row, pos_col):
    if direction == 'up':
        pos_row = row + -1
        pos_col = col
    elif direction == 'down':
        pos_row = row + 1
        pos_col = col
    elif direction == 'left':
        pos_row = row
        pos_col = col - 1
    elif direction == 'right':
        pos_row = row
        pos_col = col + 1

    return pos_row, pos_col


def create(value):
    if matrix[row][col] == '.':
        matrix[row][col] = value


def update(value):
    if matrix[row][col] != '.':
        matrix[row][col] = value


def delete():
    if matrix[row][col] != '.':
        matrix[row][col] = '.'


def read():
    if matrix[row][col] != '.':
        print(matrix[row][col])


while True:
    command = input()
    if command == 'Stop':
        break

    command = command.split(', ')
    direction = command[1]

    row, col = movement(direction, row, col)

    if command[0] == "Create":
        value = command[2]
        create(value)
    elif command[0] == "Update":
        value = command[2]
        update(value)
    elif command[0] == "Delete":
        delete()
    elif command[0] == "Read":
        read()

for line in matrix:
    print(*line)
