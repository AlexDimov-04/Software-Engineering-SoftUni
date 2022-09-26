size = int(input())
commands = input().split()
matrix = []
miner_pos = []
total_coal = 0
collected_coal = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(size):
    line = input().split()

    if 's' in line:
        miner_pos = [r, line.index('s')]
    if 'c' in line:
        total_coal += line.count('c')

    matrix.append(line)

for command in commands:
    if (miner_pos[0] + directions[command][0]) in range(size) and miner_pos[1] + directions[command][1] in range(size):
        miner_pos = [miner_pos[0] + directions[command][0], miner_pos[1] + directions[command][1]]
    if 0 <= miner_pos[0] < size and 0 <= miner_pos[1] < size:
        if matrix[miner_pos[0]][miner_pos[1]] == 'e':
            print(f"Game over! ({miner_pos[0]}, {miner_pos[1]})")
            exit()
        elif matrix[miner_pos[0]][miner_pos[1]] == 'c':
            collected_coal += 1
            matrix[miner_pos[0]][miner_pos[1]] = '*'

if collected_coal == total_coal:
    print(f"You collected all coal! ({miner_pos[0]}, {miner_pos[1]})")
else:
    print(f"{total_coal - collected_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")
