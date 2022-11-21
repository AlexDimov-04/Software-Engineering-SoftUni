from collections import deque

bomb_effects = deque(map(int, input().split(', ')))
bomb_casings = list(map(int, input().split(', ')))
bomb_types = {'Datura Bombs': {'pouch': 40, 'count': 0},
              'Cherry Bombs': {'pouch': 60, 'count': 0},
              'Smoke Decoy Bombs': {'pouch': 120, 'count': 0}}
succeeded = False

while bomb_casings and bomb_effects:
    total_sum = bomb_effects[0] + bomb_casings[-1]

    for bomb_name in bomb_types.keys():
        if total_sum == bomb_types[bomb_name]['pouch']:
            bomb_types[bomb_name]['count'] += 1
            bomb_effects.popleft()
            bomb_casings.pop()
            break
    else:
        bomb_casings[-1] -= 5

    if bomb_types['Datura Bombs']['count'] >= 3 and bomb_types['Cherry Bombs']['count'] >= 3 and \
            bomb_types['Smoke Decoy Bombs']['count'] >= 3:
        succeeded = True
        break

if not succeeded:
    print("You don't have enough materials to fill the bomb pouch.")
else:
    print("Bene! You have successfully filled the bomb pouch!")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
else:
    print("Bomb Casings: empty")

for name in sorted(bomb_types):
    print(f"{name}: {bomb_types[name]['count']}")
