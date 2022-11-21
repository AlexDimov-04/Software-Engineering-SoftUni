SIZE = int(input())
race_num = input()
car_pos = [0, 0]
race_track = []
passed_kilometers = 0
tunnels_pos = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(SIZE):
    line = input().split()

    if 'T' in line:
        tunnels_pos.append([r, line.index('T')])

    race_track.append(line)

row, col = car_pos[0], car_pos[1]


def movement(r, c, direction):
    return r + directions[direction][0], c + directions[direction][1]


while True:
    command = input()
    if command == 'End':
        print(f'Racing car {race_num} DNF.')
        break

    row, col = movement(row, col, command)

    if race_track[row][col] == '.':
        passed_kilometers += 10

    elif race_track[row][col] == 'T':
        tunnels_pos.remove([row, col])
        race_track[row][col] = '.'
        row, col = tunnels_pos[0][0], tunnels_pos[0][1]
        race_track[row][col] = '.'
        passed_kilometers += 30

    elif race_track[row][col] == 'F':
        passed_kilometers += 10
        print(f"Racing car {race_num} finished the stage!")
        break

print(f"Distance covered {passed_kilometers} km.")
race_track[row][col] = 'C'

for line in race_track:
    print(*line, sep='')
