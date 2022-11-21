from collections import deque

pumps_count = int(input())
queue = deque()

for _ in range(pumps_count):
    fuel_data = list(map(int, input().split()))
    queue.append(fuel_data)

for start in range(pumps_count):
    tank = 0
    failed = False

    for details in queue:
        fuel = details[0]
        kms = details[1]
        tank += fuel

        if kms > tank:
            failed = True
            break
        else:
            tank -= kms

    if failed:
        removed = queue.popleft()
        queue.append(removed)
    else:
        print(start)
        break
