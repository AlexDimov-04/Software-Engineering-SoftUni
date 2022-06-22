max_health = 100
is_dead = False

rooms = input().split('|')

health = max_health
bitcoins = 0
best_room = 0

for i in range(len(rooms)):
    best_room += 1
    command = rooms[i]
    tokens = command.split()

    if tokens[0] == 'potion':
        health_points = int(tokens[1])
        if health + health_points > max_health:
            health_points = max_health - health
            health = max_health
        else:
            health += health_points
        print(f'You healed for {health_points} hp.')
        print(f'Current health: {health} hp.')

    elif tokens[0] == 'chest':
        amount = int(tokens[1])
        print(f'You found {amount} bitcoins.')
        bitcoins += amount
    else:
        monster = tokens[0]
        attack = int(tokens[1])
        health -= attack
        if health > 0:
            print(f'You slayed {monster}.')
        else:
            print(f'You died! Killed by {monster}.')
            print(f'Best room: {best_room}')
            is_dead = True
            break

if not is_dead:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")