from collections import deque

cups_capacity = deque(map(int, input().split()))
filled_bottles = list(map(int, input().split()))  # stack
extract_diff = 0

while True:
    cup = cups_capacity.popleft()
    bottle = filled_bottles.pop()

    if bottle >= cup:
        extract_diff += bottle - cup
    else:
        cup -= bottle
        cups_capacity.appendleft(cup)

    if not cups_capacity:
        print(f"Bottles: {' '.join(str(x) for x in filled_bottles[::-1])}")
        break
    elif not filled_bottles:
        print(f"Cups: {' '.join(str(x) for x in cups_capacity)}")
        break

print(f"Wasted litters of water: {extract_diff}")
