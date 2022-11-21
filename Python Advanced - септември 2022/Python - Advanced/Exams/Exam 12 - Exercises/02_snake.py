SIZE = int(input())
matrix = []
snake_pos = []
burrows_pos = []
eaten_food = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(SIZE):
    line = list(input())

    if 'S' in line:
        snake_pos = [r, line.index('S')]
        line[line.index('S')] = '.'

    if 'B' in line:
        if line.count('B') == 1:
            burrows_pos.append([r, line.index('B')])
        else:
            for idx, el in enumerate(line):
                if el == 'B':
                    burrows_pos.append([r, idx])

    matrix.append(line)


def valid(r, c):
    return 0 <= r < SIZE and 0 <= c < SIZE


def movement(r, c, direction):
    return r + directions[direction][0], c + directions[direction][1]


def output(food_consumed):
    print(f"Food eaten: {food_consumed}")
    for l in matrix:
        print(*l, sep='')


row, col = snake_pos[0], snake_pos[1]

while True:
    command = input()
    row, col = movement(row, col, command)

    if valid(row, col):
        if matrix[row][col] == '*':
            eaten_food += 1
            matrix[row][col] = '.'

        elif matrix[row][col] == 'B':
            burrows_pos.remove([row, col])
            matrix[row][col] = '.'
            row, col = burrows_pos[0][0], burrows_pos[0][1]
            matrix[row][col] = '.'

        else:
            matrix[row][col] = '.'
    else:
        print("Game over!")
        output(eaten_food)
        break

    if eaten_food == 10:
        print("You won! You fed the snake.")
        matrix[row][col] = 'S'
        output(eaten_food)
        break
