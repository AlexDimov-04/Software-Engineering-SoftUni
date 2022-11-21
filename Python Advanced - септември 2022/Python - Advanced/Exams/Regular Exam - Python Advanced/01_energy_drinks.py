from collections import deque

MAX_CAFFEINE_FOR_NIGHT = 300
caffeine = list(map(int, input().split(', ')))
energy_drinks = deque(map(int, input().split(', ')))
initial_caffeine = 0

while caffeine and energy_drinks:
    mixed = caffeine[-1] * energy_drinks[0]

    if mixed + initial_caffeine <= MAX_CAFFEINE_FOR_NIGHT:
        initial_caffeine += mixed
        caffeine.pop()
        energy_drinks.popleft()

    else:
        caffeine.pop()
        energy_drinks.append(energy_drinks.popleft())
        if initial_caffeine:
            initial_caffeine -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {initial_caffeine} mg caffeine.")
