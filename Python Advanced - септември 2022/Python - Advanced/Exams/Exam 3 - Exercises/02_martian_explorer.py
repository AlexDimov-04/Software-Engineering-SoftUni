ROWS, COLS = 6, 6
board = []
rover_pos = []
deposits = []

for r in range(ROWS):
    line = input().split()

    if 'E' in line:
        rover_pos = [r, line.index('E')]

    board.append(line)

coords = [x for x in input().split(', ')]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


def deposit_placement(r, c):
    if board[r][c] == 'W':
        print(f"Water deposit found at ({r}, {c})")
        deposits.append('W')


    elif board[r][c] == 'M':
        print(f"Metal deposit found at ({r}, {c})")
        deposits.append('M')

    elif board[r][c] == 'C':
        print(f"Concrete deposit found at ({r}, {c})")
        deposits.append('C')


for direction in coords:
    rover_pos = [rover_pos[0] + directions[direction][0], rover_pos[1] + directions[direction][1]]

    if not 0 <= rover_pos[0] < ROWS or not 0 <= rover_pos[1] < COLS:
        if rover_pos[1] == -1:  # left
            rover_pos[1] = 5

        elif rover_pos[1] == 6:  # right
            rover_pos[1] = 0

        elif rover_pos[0] == -1:  # up
            rover_pos[0] = 5

        elif rover_pos[0] == 6:  # down
            rover_pos[0] = 0

    if board[rover_pos[0]][rover_pos[1]] in 'WMC':
        deposit_placement(rover_pos[0], rover_pos[1])

    elif board[rover_pos[0]][rover_pos[1]] == 'R':
        print(f"Rover got broken at ({rover_pos[0]}, {rover_pos[1]})")
        break

if 'W' in deposits and 'M' in deposits and 'C' in deposits:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
