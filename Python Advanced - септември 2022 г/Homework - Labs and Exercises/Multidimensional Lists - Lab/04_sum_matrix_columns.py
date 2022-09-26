rows, cols = list(map(int, input().split(', ')))
matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

for col in range(cols):
    total_sum = 0
    for row in range(rows):
        total_sum += matrix[row][col]
    print(total_sum)
