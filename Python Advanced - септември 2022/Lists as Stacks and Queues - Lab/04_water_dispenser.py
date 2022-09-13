from collections import deque

water = int(input())
queue = deque()

while True:
    name = input()
    if name == "Start":
        break

    queue.append(name)

while True:
    command = input()
    if command == "End":
        print(f"{water} liters left")
        break

    command = command.split()
    if command[0] == "refill":
        liters = int(command[1])
        water += liters
    else:
        liters = int(command[0])
        if liters <= water:
            person = queue.popleft()
            print(f"{person} got water")
            water -= liters
        else:
            person = queue.popleft()
            print(f"{person} must wait")
