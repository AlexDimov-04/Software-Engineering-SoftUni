ROWS, COLS = 6, 6
matrix = [[x for x in input().split()] for _ in range(ROWS)]
total_score = 0

for command in range(3):
    coord_1, coord_2 = input().replace(',', '').strip('()').split()

    row, col = int(coord_1), int(coord_2)

    if 0 <= row < ROWS and 0 <= col < COLS:
        if matrix[row][col] == 'B':
            matrix[row][col] = '.'
            for r in range(ROWS):
                if matrix[r][col].isdigit():
                    total_score += int(matrix[r][col])

if total_score < 100:
    print(f"Sorry! You need {100 - total_score} points more to win a prize.")

elif 100 <= total_score <= 199:
    print(f"Good job! You scored {total_score} points, and you've won Football.")

elif 200 <= total_score <= 299:
    print(f"Good job! You scored {total_score} points, and you've won Teddy Bear.")

else:
    print(f"Good job! You scored {total_score} points, and you've won Lego Construction Set.")
