rows, cols = list(map(int, input().split()))
matrix = []

for row in range(rows):
    elements = []
    for col in range(cols):
        result = chr(97 + row) + chr(97 + row + col) + chr(97 + row)
        elements.append(result)

    matrix.append(elements)

for lst in matrix:
    print(*lst)
