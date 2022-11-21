from collections import deque

ROWS, COLS = 8, 8
board = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
black_pos = []
white_pos = []
players = deque(['w', 'b'])

directions = (
    [-1, -1],  # up-left
    [-1, 1],  # up-right
    [1, -1],  # down-left
    [1, 1]  # down-right
)

for r in range(ROWS):
    line = input().split()

    if 'b' in line:
        black_pos = [r, line.index('b')]

    if 'w' in line:
        white_pos = [r, line.index('w')]

    board.append(line)

while True:
    player = players[0]

    if white_pos[1] - black_pos[1] == 1 or white_pos[1] - black_pos[1] == -1:
        for direction in directions:
            if player == 'w':
                row, col = direction[0] + white_pos[0], direction[1] + white_pos[1]

                if 0 <= row < ROWS and 0 <= col < COLS:
                    if board[row][col] == 'b':
                        print(f"Game over! White win, capture on {letters[col] + str((abs(row - ROWS)))}.")
                        exit()

            elif player == 'b':
                row, col = direction[0] + black_pos[0], direction[1] + black_pos[1]

                if 0 <= row < ROWS and 0 <= col < COLS:
                    if board[row][col] == 'w':
                        print(f"Game over! Black win, capture on {letters[col] + str((abs(row - ROWS)))}.")
                        exit()
    else:
        if player == 'w':
            white_pos[0] -= 1

        elif player == 'b':
            black_pos[0] += 1

        if white_pos[0] == 0:
            letter = white_pos[1]
            print(f"Game over! White pawn is promoted to a queen at {letters[letter] + '8'}.")
            break

        elif black_pos[0] == 7:
            letter = white_pos[1]
            print(f"Game over! Black pawn is promoted to a queen at {letters[letter] + '1'}.")
            break

    players.append(players.popleft())
