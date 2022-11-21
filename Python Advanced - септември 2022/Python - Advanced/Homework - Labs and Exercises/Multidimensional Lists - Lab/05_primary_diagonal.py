n = int(input())
matrix = []
total_sum = 0

for _ in range(n):
    matrix.append(list(map(int, input().split())))

for idx in range(n):
    total_sum += matrix[idx][idx]

print(total_sum)
