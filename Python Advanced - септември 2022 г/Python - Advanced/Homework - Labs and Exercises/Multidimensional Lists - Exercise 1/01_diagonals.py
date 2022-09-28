rows = int(input())
matrix = [list(map(int, input().split(', '))) for _ in range(rows)]
primary_diag = []
secondary_diag = []


for idx in range(rows):
    primary_diag.append(matrix[idx][idx])
    secondary_diag.append(matrix[idx][rows - idx - 1])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diag)}. Sum: {sum(primary_diag)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diag)}. Sum: {sum(secondary_diag)}")
