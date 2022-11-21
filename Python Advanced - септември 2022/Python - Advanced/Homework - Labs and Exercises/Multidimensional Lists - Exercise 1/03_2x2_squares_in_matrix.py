rows, cols = list(map(int, input().split()))
matrix = [input().split() for _ in range(rows)]
counter = 0

for row in range(rows):
    if row == rows - 1:
        break
    for col in range(len(matrix[row])):
        if col == cols - 1:
            break

        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            counter += 1

print(counter)
