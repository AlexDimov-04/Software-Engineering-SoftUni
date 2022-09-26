rows = int(input())
matrix = [list(map(int, input().split())) for _ in range(rows)]

while True:
    command = input()
    if command == "END":
        for row in matrix:
            print(*row)
        break

    command = command.split()
    if 'Add' in command:
        row, col, value = command[1:]
        if int(row) in range(len(matrix)) and int(col) in range(len(matrix)):
            matrix[int(row)][int(col)] += int(value)
        else:
            print("Invalid coordinates")
    elif 'Subtract' in command:
        row, col, value = command[1:]
        if int(row) in range(len(matrix)) and int(col) in range(len(matrix)):
            matrix[int(row)][int(col)] -= int(value)
        else:
            print("Invalid coordinates")
