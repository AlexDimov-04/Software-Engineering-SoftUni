def move(direction, steps):
    r = my_position[0] + (directions[direction][0] * steps)
    c = my_position[1] + (directions[direction][1] * steps)

    if not (0 <= r < size and 0 <= c < size):
        return my_position
    if field[r][c] == 'x':
        return my_position
    return [r, c]


def shoot(direction):
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]

    while r in range(len(field)) and c in range(len(field)):
        if field[r][c] == 'x':
            field[r][c] = '.'
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


size = 5
field = []

targets = 0
targets_hit = 0
targets_hit_positions = []

my_position = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    line = input().split()

    field.append(line)

    if 'A' in line:
        my_position = [row, line.index('A')]
        field[my_position[0]][my_position[1]] = '.'

    targets += line.count('x')

for _ in range(int(input())):
    command = input().split()

    if command[0] == 'move':
        my_position = move(command[1], int(command[2]))
    elif command[0] == 'shoot':
        target_down_pos = shoot(command[1])

        if target_down_pos:
            targets_hit_positions.append(target_down_pos)
            targets_hit += 1

        if targets_hit == targets:
            print(f"Training completed! All {targets} targets hit.")
            break

if targets_hit < targets:
    print(f"Training not completed! {targets - targets_hit} targets left.")

for line in targets_hit_positions:
    print(line)
