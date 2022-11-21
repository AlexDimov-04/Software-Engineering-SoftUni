SIZE = int(input())
bombs = int(input())
matrix = [[x for x in '0' * SIZE] for _ in range(SIZE)]

directions = {
    "up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0),
    "top left diagonal": (-1, -1), "bottom left diagonal": (-1, 1),
    "top right diagonal": (1, -1), "bottom right diagonal": (1, 1)}

for bomb in range(bombs):
    bomb_row, bomb_col = input().replace(',', '').strip('()').split()
    matrix[int(bomb_row)][int(bomb_col)] = '*'


def valid(row, col):
    return 0 <= row < SIZE and 0 <= col < SIZE


def check_bombs(row, col):
    sum_bombs = 0
    for move_row, move_col in directions.values():
        current_row, current_col = row + move_row, col + move_col

        if valid(current_row, current_col) and matrix[current_row][current_col] == '*':
            sum_bombs += 1
            matrix[row][col] = sum_bombs


for row in range(SIZE):
    for col in range(SIZE):
        if matrix[row][col] != '*':
            check_bombs(row, col)

for line in matrix:
    print(*line)
