ROWS, COLS = 7, 7

first_player, second_player = input().split(', ')
dartboard = [[x for x in input().split()] for _ in range(ROWS)]
throws = {first_player: 0, second_player: 0}
points = {first_player: 501, second_player: 501}
players = [first_player, second_player]

while True:
    r, c = input().replace(',', '').strip('()').split()
    row, col = int(r), int(c)
    player = players.pop(0)

    throws[player] += 1

    if 0 <= row < ROWS and 0 <= col < COLS:
        if dartboard[row][col].isdigit():
            points[player] -= int(dartboard[row][col])

        elif dartboard[row][col] == 'D':
            total = int(dartboard[row][0]) + int(dartboard[row][6]) + int(dartboard[0][col]) + int(dartboard[6][col])
            points[player] -= total * 2

        elif dartboard[row][col] == 'T':
            total = int(dartboard[row][0]) + int(dartboard[row][6]) + int(dartboard[0][col]) + int(dartboard[6][col])
            points[player] -= total * 3

        elif dartboard[row][col] == 'B':
            print(f"{player} won the game with {throws[player]} throws!")
            break

        if points[player] <= 0:
            print(f"{player} won the game with {throws[player]} throws!")
            break

    players.append(player)
