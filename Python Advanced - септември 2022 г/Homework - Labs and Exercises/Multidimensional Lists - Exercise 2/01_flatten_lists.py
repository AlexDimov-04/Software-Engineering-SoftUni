numbers = input().split('|')[::-1]

matrix = []

for el in numbers:
    matrix.extend(el.split())

print(*matrix)
