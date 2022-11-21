from collections import deque

ramen = list(map(int, input().split(', ')))
customers = deque(map(int, input().split(', ')))

while ramen and customers:
    if ramen[-1] == customers[0]:
        ramen.pop()
        customers.popleft()

    elif ramen[-1] > customers[0]:
        ramen[-1] -= customers[0]
        customers.popleft()

    elif ramen[-1] < customers[0]:
        customers[0] -= ramen[-1]
        ramen.pop()

if not customers:
    print("Great job! You served all the customers.")
    if ramen:
        print(f"Bowls of ramen left: {', '.join(map(str, ramen))}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join(map(str, customers))}")
