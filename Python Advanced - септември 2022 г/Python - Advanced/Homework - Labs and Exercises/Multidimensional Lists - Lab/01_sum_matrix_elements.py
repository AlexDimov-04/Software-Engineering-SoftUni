rows, cols = list(map(int, input().split(', ')))
matrix = []
total_sum = 0

for i in range(rows):
    matrix.append(list(map(int, input().split(', '))))

for row in range(rows):
    for col in range(cols):
        total_sum += matrix[row][col]

print(total_sum)
print(matrix)
