size = int(input())
matrix = [list(input()) for _ in range(size)]
removed_knights = 0

positions = (
    (2, -1),
    (2, 1),
    (1, -2),
    (1, 2),
    (-1, -2),
    (-1, 2),
    (-2, -1),
    (-2, 1)
)

while True:
    max_attacks = 0
    knight_most_attacks = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'K':
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]
                    if pos_row in range(len(matrix)) and pos_col in range(len(matrix)):
                        if matrix[pos_row][pos_col] == 'K':
                            attacks += 1

                if attacks > max_attacks:
                    knight_most_attacks = [row, col]
                    max_attacks = attacks

    if knight_most_attacks:
        matrix[knight_most_attacks[0]][knight_most_attacks[1]] = '0'
        removed_knights += 1
    else:
        break

print(removed_knights)
