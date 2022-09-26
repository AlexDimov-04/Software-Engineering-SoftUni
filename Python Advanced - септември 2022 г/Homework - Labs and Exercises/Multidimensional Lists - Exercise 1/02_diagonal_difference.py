size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]

primary_diagonal = []
secondary_diagonal = []

for idx in range(size):
    primary_diagonal.append(matrix[idx][idx])
    secondary_diagonal.append(matrix[idx][size - idx - 1])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
