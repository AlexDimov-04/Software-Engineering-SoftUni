from collections import deque

pizzas = deque(map(int, input().split(', ')))
employees = list(map(int, input().split(', ')))
pizzas_count = 0

while pizzas and employees:

    if pizzas[0] > 10 or pizzas[0] <= 0:
        pizzas.popleft()

    elif pizzas[0] <= employees[-1]:
        pizzas_count += pizzas[0]
        employees.pop()
        pizzas.popleft()

    elif pizzas[0] > employees[-1]:
        pizzas[0] -= employees[-1]
        pizzas_count += employees[-1]
        employees.pop()

if not pizzas:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas_count}")
    print(f"Employees: {', '.join(map(str, employees))}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, pizzas))}")
