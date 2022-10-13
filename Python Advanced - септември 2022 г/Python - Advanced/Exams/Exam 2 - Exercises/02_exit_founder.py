from collections import deque

names = deque(input().split(', '))
size = 6
maze_board = [input().split() for _ in range(size)]
iteration = 0
rested_player = ''

while True:
    iteration += 1
    data = input()
    coords = [int(x) for x in data if x.isdigit()]
    player = names.popleft()

    if iteration % 2 != 0 and rested_player:
        names.append(player)
        rested_player = ''
        continue

    if maze_board[coords[0]][coords[1]] == 'E':
        print(f"{player} found the Exit and wins the game!")
        break

    elif maze_board[coords[0]][coords[1]] == 'T':
        print(f"{player} is out of the game! The winner is {''.join(names)}.")
        break

    elif maze_board[coords[0]][coords[1]] == 'W':
        print(f"{player} hits a wall and needs to rest.")
        rested_player = player

    names.append(player)
