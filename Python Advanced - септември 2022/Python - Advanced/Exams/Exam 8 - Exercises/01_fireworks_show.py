from collections import deque

fireworks = deque(map(int, input().split(', ')))
explosives = list(map(int, input().split(', ')))
palm = 0
willow = 0
crossette = 0
needed_fireworks = False

while fireworks and explosives:

    if fireworks[0] <= 0 or explosives[-1] <= 0:
        if fireworks[0] <= 0:
            fireworks.popleft()

        if explosives[-1] <= 0:
            explosives.pop()

        continue

    total = fireworks[0] + explosives[-1]

    if total % 3 == 0 and total % 5 == 0:
        crossette += 1
        fireworks.popleft()
        explosives.pop()

    elif total % 3 == 0:
        palm += 1
        fireworks.popleft()
        explosives.pop()

    elif total % 5 == 0:
        willow += 1
        fireworks.popleft()
        explosives.pop()

    else:
        fireworks[0] -= 1
        fireworks.append(fireworks.popleft())

    if palm + willow + crossette >= 9:
        needed_fireworks = True
        break

if needed_fireworks:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks:
    print(f"Firework Effects left: {', '.join(map(str, fireworks))}")
if explosives:
    print(f"Explosive Power left: {', '.join(map(str, explosives))}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")
