def get_magic_triangle(n):
    matrix = []

    for row in range(n):
        matrix.append([])
        matrix[row].append(1)
        for col in range(1, row):
            matrix[row].append(matrix[row - 1][col - 1] + matrix[row - 1][col])

        if row != 0:
            matrix[row].append(1)

    return matrix
