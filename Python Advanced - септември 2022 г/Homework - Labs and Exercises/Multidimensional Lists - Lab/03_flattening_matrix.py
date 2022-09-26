n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split(', '))))

# output = []
# for el in matrix:
#     output.extend(el)
# print(output)

print(list(num for sublist in matrix for num in sublist))
