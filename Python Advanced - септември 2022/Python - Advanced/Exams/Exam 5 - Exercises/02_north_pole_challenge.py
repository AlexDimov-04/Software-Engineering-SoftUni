ROWS, COLS = list(map(int, input().split(', ')))
santa_pos = []
matrix = []

collected_items = {'Christmas decorations': 0, 'Gifts': 0, 'Cookies': 0}

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(ROWS):
    line = input().split()

    matrix.append(line)

    if 'Y' in line:
        santa_pos = [r, line.index('Y')]
        matrix[r][line.index('Y')] = 'x'


def output_result():
    print("You've collected:")
    for item, count in collected_items.items():
        print(f"- {count} {item}")

    matrix[santa_pos[0]][santa_pos[1]] = 'Y'

    for row in matrix:
        print(*row)


def check_items():
    found = False
    for line in matrix:
        items_spotted = [x for x in line if x.isupper()]

        if items_spotted:
            return True

    if not found:
        print("Merry Christmas!")
        output_result()
        raise SystemExit


def items(row, col):
    if matrix[row][col] == 'D':
        collected_items['Christmas decorations'] += 1

    elif matrix[row][col] == 'G':
        collected_items['Gifts'] += 1

    elif matrix[row][col] == 'C':
        collected_items['Cookies'] += 1


while True:
    command = input()
    if command == 'End':
        matrix[santa_pos[0]][santa_pos[1]] = 'Y'
        break

    direction, steps = command.split('-')
    remaining_steps = int(steps)

    try:
        if direction == 'up':
            for _ in range(1, int(steps) + 1):
                santa_pos[0] -= 1
                items(santa_pos[0], santa_pos[1])
                matrix[santa_pos[0]][santa_pos[1]] = 'x'

                remaining_steps -= 1
                check_items()

        elif direction == 'down':
            for _ in range(1, int(steps) + 1):
                santa_pos[0] += 1
                items(santa_pos[0], santa_pos[1])
                matrix[santa_pos[0]][santa_pos[1]] = 'x'

                remaining_steps -= 1
                check_items()

        elif direction == 'left':
            for _ in range(1, int(steps) + 1):
                santa_pos[1] -= 1
                items(santa_pos[0], santa_pos[1])
                matrix[santa_pos[0]][santa_pos[1]] = 'x'

                remaining_steps -= 1
                check_items()

        elif direction == 'right':
            for _ in range(1, int(steps) + 1):
                santa_pos[1] += 1
                items(santa_pos[0], santa_pos[1])
                matrix[santa_pos[0]][santa_pos[1]] = 'x'

                remaining_steps -= 1
                check_items()

    except IndexError:
        if direction == 'up':
            santa_pos[0] = ROWS - 1

            for _ in range(1, remaining_steps + 1):
                santa_pos[0] += 1
                items(santa_pos[0], santa_pos[1])
                matrix[santa_pos[0]][santa_pos[1]] = 'x'

                check_items()

        elif direction == 'down':
            santa_pos[0] = 0

            for _ in range(1, remaining_steps + 1):
                santa_pos[0] += 1
                items(santa_pos[0], santa_pos[1])
                matrix[santa_pos[0]][santa_pos[1]] = 'x'

                check_items()

        elif direction == 'left':
            santa_pos[1] = COLS - 1

            for _ in range(1, remaining_steps + 1):
                santa_pos[1] -= 1
                items(santa_pos[0], santa_pos[1])
                matrix[santa_pos[0]][santa_pos[1]] = 'x'

                check_items()

        elif direction == 'right':
            santa_pos[1] = 0

            for _ in range(1, remaining_steps + 1):
                santa_pos[1] += 1
                items(santa_pos[0], santa_pos[1])
                matrix[santa_pos[0]][santa_pos[1]] = 'x'

                check_items()

output_result()
