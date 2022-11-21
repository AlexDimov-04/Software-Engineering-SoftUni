import math

SIZE = int(input())
matrix = []
player_pos = []
player_path = []
coins = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(SIZE):
    line = input().split()

    if 'P' in line:
        player_pos = [r, line.index('P')]
        player_path.append([r, line.index('P')])

    matrix.append(line)


def check_position(r, c):
    global coins
    if matrix[r][c].isdigit():
        coins += float(matrix[r][c])
        matrix[r][c] = '.'

    elif matrix[r][c] == 'X':
        coins /= 2.0
        print(f"Game over! You've collected {math.floor(coins)} coins.")
        print(f"Your path:")
        print(*player_path, sep='\n')
        exit()


while True:
    command = input()

    player_pos = [player_pos[0] + directions[command][0], player_pos[1] + directions[command][1]]
    row, col = player_pos

    if 0 <= row < SIZE and 0 <= col < SIZE:
        player_path.append([row, col])
        check_position(row, col)
    else:
        if col == -1:
            col = SIZE - 1

        elif col == SIZE:
            col = 0

        elif row == -1:
            row = SIZE - 1

        elif row == SIZE:
            row = 0

        player_path.append([row, col])
        player_pos = [row, col]
        check_position(row, col)

    if coins >= 100:
        print(f"You won! You've collected {math.floor(coins)} coins.")
        print(f"Your path:")
        print(*player_path, sep='\n')
        break
