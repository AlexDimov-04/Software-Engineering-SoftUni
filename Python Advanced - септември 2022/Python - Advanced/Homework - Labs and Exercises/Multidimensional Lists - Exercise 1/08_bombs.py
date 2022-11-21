from collections import deque

size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]
coords = deque(map(int, input().replace(',', ' ').split()))
alive_cells = []

directions = (
    (-1, 0),  # up
    (1, 0),  # down
    (0, -1),  # left
    (0, 1),  # right
    (-1, -1),  # up-left
    (-1, 1),  # up-right
    (1, -1),  # down-left
    (1, 1)  # down-right
)

while coords:
    row, col = coords.popleft(), coords.popleft()
    if matrix[row][col] > 0:
        for direction in directions:
            pos_row = row + direction[0]
            pos_col = col + direction[1]

            if 0 <= pos_row < size and 0 <= pos_col < size:
                if matrix[pos_row][pos_col] > 0:
                    matrix[pos_row][pos_col] -= matrix[row][col]

        matrix[row][col] -= matrix[row][col]

for line in matrix:
    alive = [x for x in line if x > 0]
    alive_cells.extend(alive)

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

for line in matrix:
    print(*line)
