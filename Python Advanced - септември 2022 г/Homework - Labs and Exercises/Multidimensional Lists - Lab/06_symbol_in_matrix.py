n = int(input())
matrix = []

for _ in range(n):
    matrix.append(input())

symbol = input()

for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            exit()

print(f"{symbol} does not occur in the matrix")
