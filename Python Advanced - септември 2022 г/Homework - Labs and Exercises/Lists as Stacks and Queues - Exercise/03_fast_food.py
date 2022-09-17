from collections import deque

total_food = int(input())
orders = deque(map(int, input().split()))

print(max(orders))
while orders:
    current_order = orders.popleft()
    if current_order <= total_food:
        total_food -= current_order
    else:
        print(f"Orders left: {current_order}", *orders)
        exit()

print("Orders complete")
