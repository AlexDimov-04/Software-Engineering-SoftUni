from collections import deque

chocolates = list(map(int, input().split(', ')))  # chocolates/stack
milk_cups = deque((map(int, input().split(', '))))  # milk/queue
milkshakes = 0

while milkshakes < 5 and chocolates and milk_cups:
    if chocolates[-1] <= 0 and milk_cups[0] <= 0:
        chocolates.pop()
        milk_cups.popleft()
        continue

    if chocolates[-1] <= 0:
        chocolates.pop()
        continue

    if milk_cups[0] <= 0:
        milk_cups.popleft()
        continue

    if chocolates[-1] == milk_cups[0]:
        chocolates.pop()
        milk_cups.popleft()
        milkshakes += 1

    else:
        milk_cups.append(milk_cups.popleft())
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) if chocolates else 'empty'}")
print(f"Milk: {', '.join(str(x) for x in milk_cups) if milk_cups else 'empty'}")
