from collections import deque

queue = deque()

while True:
    name = input()
    if name == "End":
        print(f"{len(queue)} people remaining.")
        break

    elif name == "Paid":
        print('\n'.join(queue))
        queue.clear()
        continue

    queue.append(name)
