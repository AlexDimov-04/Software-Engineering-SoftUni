elements = [i for i in input().split()]
move = 0
won_game = False

while True:
    command = input()
    if command == 'end':
        break

    command = command.split()
    index_1 = int(command[0])
    index_2 = int(command[-1])
    move += 1

    if elements[index_1] == elements[index_2]:
        print(f"Congrats! You have found matching elements - {elements[index_1]}!")
        remove_from_list = elements[index_1]
        elements.remove(remove_from_list)
        elements.remove(remove_from_list)
    elif index_2 == index_1 or index_2 < 0 or index_1 < 0 \
            or len(elements) - 1 < index_1 or len(elements) - 1 < index_2:
        print("Invalid input! Adding additional elements to the board")
        middle = int(len(elements) / 2)
        elements.insert(middle, str(-move) + "a")
        elements.insert(middle, str(-move) + "a")
    else:
        print('Try again!')

    if len(elements) == 0:
        won_game = True
        break

if won_game:
    print(f'You have won in {move} turns!')
else:
    print("Sorry you lose :(")
    print(' '.join(str(x) for x in elements))

