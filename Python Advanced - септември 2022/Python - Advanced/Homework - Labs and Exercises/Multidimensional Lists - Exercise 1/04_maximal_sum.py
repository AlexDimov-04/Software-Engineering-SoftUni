from sys import maxsize

rows, cols = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(rows)]
biggest_square = []
biggest_square_sum = -maxsize

for row in range(rows - 2):
    for col in range(cols - 2):

        square = [
            [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
            [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
            [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
        ]

        square_sum = sum([num for sublist in square for num in sublist])
        if square_sum > biggest_square_sum:
            biggest_square_sum = square_sum
            biggest_square = square

print(f"Sum = {biggest_square_sum}")
for elements in biggest_square:
    print(*elements)