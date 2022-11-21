text = input()
SIZE = int(input())
player_pos = []
field = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(SIZE):
    line = list(input())

    if 'P' in line:
        player_pos = [r, line.index('P')]

    field.append(line)

field[player_pos[0]][player_pos[1]] = '-'

commands = int(input())

for n in range(commands):
    command = input()

    if player_pos[0] + directions[command][0] in range(SIZE) and player_pos[1] + directions[command][1] in range(SIZE):
        player_pos = [player_pos[0] + directions[command][0], player_pos[1] + directions[command][1]]

        if field[player_pos[0]][player_pos[1]].isalpha():
            text += field[player_pos[0]][player_pos[1]]
            field[player_pos[0]][player_pos[1]] = '-'

    else:
        if text:
            text = text[:-1]

field[player_pos[0]][player_pos[1]] = 'P'

print(text)
for line in field:
    print(*line, sep='')
