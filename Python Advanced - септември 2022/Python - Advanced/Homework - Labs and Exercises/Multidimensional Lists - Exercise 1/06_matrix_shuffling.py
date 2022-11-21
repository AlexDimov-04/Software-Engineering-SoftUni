rows, cols = list(map(int, input().split()))
matrix = [input().split() for _ in range(rows)]

while True:
    command = input()
    if command == "END":
        break

    command = command.split()

    if len(command) == 5 and 'swap' in command:
        rol1, col1, row2, col2 = command[1:]
        if int(rol1) in range(len(matrix)) or int(col1) in range(len(matrix)) or int(row2) in range(len(matrix)) or int(
                col2) in range(len(matrix)):
            matrix[int(rol1)][int(col1)], matrix[int(row2)][int(col2)] = matrix[int(row2)][int(col2)], \
                                                                         matrix[int(rol1)][
                                                                             int(col1)]
        else:
            print("Invalid input!")
            continue
        for elements in matrix:
            print(*elements)
    else:
        print("Invalid input!")
