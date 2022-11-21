rows, cols = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(rows)]
max_sum = 0
values = []

for row in range(rows):
    if row == rows - 1:
        break
    for col in range(len(matrix[row])):
        if col == cols - 1:
            break

        if matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1] > max_sum:
            max_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
            values.clear()
            values.append(matrix[row][col])
            values.append(matrix[row][col + 1])
            values.append(matrix[row + 1][col])
            values.append(matrix[row + 1][col + 1])

print(f"{values[0]} {values[1]}\n{values[2]} {values[3]}")
print(max_sum)
