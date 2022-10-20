SIZE = 8
matrix, king_pos, queen_captures = [], [], []

directions = {
    'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0),
    'top left diagonal': (-1, -1), 'bottom left diagonal': (-1, 1),
    'top right diagonal': (1, -1), 'bottom right diagonal': (1, 1)
}

for r in range(SIZE):
    line = input().split()

    if 'K' in line:
        king_pos = [r, line.index('K')]

    matrix.append(line)


def valid(row, col):
    return 0 <= row < SIZE and 0 <= col < SIZE


def movement(row, col, direction):
    return row + directions[direction][0], col + directions[direction][1]


for direction in directions:
    r, c = king_pos[0], king_pos[1]
    for step in range(SIZE):
        r, c = movement(r, c, direction)

        if valid(r, c):
            if matrix[r][c] == 'Q':
                queen_captures.append([r, c])
                break

        else:
            break

if queen_captures:
    print(*queen_captures, sep='\n')
else:
    print('The king is safe!')
