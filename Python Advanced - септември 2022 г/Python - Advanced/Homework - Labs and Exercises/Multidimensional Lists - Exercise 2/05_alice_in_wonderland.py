size = int(input())

matrix = []
alise_pos = []

tea_bags = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(size):
    line = input().split()
    matrix.append(line)

    if 'A' in line:
        alise_pos = [r, line.index('A')]
        matrix[r][alise_pos[1]] = '*'

while tea_bags < 10:
    direction = input()

    row = alise_pos[0] + directions[direction][0]
    col = alise_pos[1] + directions[direction][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    alice_pos = [row, col]
    position = matrix[row][col]
    matrix[row][col] = '*'

    if position == 'R':
        break

    if position.isdigit():
        tea_bags += int(position)

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for line in matrix:
    print(*line)
