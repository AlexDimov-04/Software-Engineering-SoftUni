from collections import deque

elves_energy = deque(list(map(int, input().split())))
materials = list(map(int, input().split()))
total_energy = 0
toys = 0
cookie_reward = 1
iteration = 0

while elves_energy and materials:

    if elves_energy[0] < 5:
        elves_energy.popleft()
        continue

    iteration += 1

    if iteration % 3 == 0:

        if elves_energy[0] >= materials[-1] * 2:

            if iteration % 5 == 0:
                elves_energy[0] -= materials[-1] * 2
            else:
                toys += 2
                elves_energy[0] += cookie_reward
                elves_energy[0] -= materials[-1] * 2

            total_energy += materials[-1] * 2
            materials.pop()
            elves_energy.append(elves_energy.popleft())

        else:
            elves_energy[0] *= 2
            elves_energy.append(elves_energy.popleft())

    else:

        if elves_energy[0] >= materials[-1]:

            if iteration % 5 == 0:
                elves_energy[0] -= materials[-1]
            else:
                toys += 1
                elves_energy[0] += cookie_reward
                elves_energy[0] -= materials[-1]

            total_energy += materials[-1]
            materials.pop()
            elves_energy.append(elves_energy.popleft())

        else:
            elves_energy[0] *= 2
            elves_energy.append(elves_energy.popleft())

print(f"Toys: {toys}")
print(f"Energy: {total_energy}")

if elves_energy:
    print(f"Elves left: {', '.join(str(x) for x in elves_energy)}")
if materials:
    print(f"Boxes left: {', '.join(str(x) for x in materials)}")
