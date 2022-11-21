from collections import deque

bees = deque(map(int, input().split()))  # queue
nectars = list(map(int, input().split()))  # stack
symbols = deque(input().split())
total_honey = 0

while bees and nectars:
    if nectars[-1] >= bees[0]:
        symbol = symbols.popleft()
        nectar, bee = nectars.pop(), bees.popleft()
        if symbol == "+":
            total_honey += abs(bee + nectar)
        elif symbol == "-":
            total_honey += abs(bee - nectar)
        elif symbol == "*":
            total_honey += abs(bee * nectar)
        elif symbol == "/" and bee != 0 or nectar != 0:
            total_honey += abs(bee / nectar)
    else:
        nectars.pop()

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectars:
    print(f"Nectar left: {', '.join(str(x) for x in nectars)}")
