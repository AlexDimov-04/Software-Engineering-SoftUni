from collections import deque

seats = input().split(', ')
seq_1 = deque(map(int, input().split(', ')))
seq_2 = deque(map(int, input().split(', ')))
rotations = 0
seat_matches = []

while rotations < 10:
    character = chr(seq_1[0] + seq_2[-1])

    combination_1 = str(seq_1[0]) + character
    combination_2 = str(seq_2[-1]) + character

    if combination_1 in seat_matches or combination_2 in seat_matches:
        seq_1.popleft()
        seq_2.pop()

    elif combination_1 in seats:
        seat_matches.append(combination_1)
        seq_1.popleft()
        seq_2.pop()

    elif combination_2 in seats:
        seat_matches.append(combination_2)
        seq_1.popleft()
        seq_2.pop()
    else:
        seq_1.append(seq_1.popleft())
        seq_2.appendleft(seq_2.pop())

    rotations += 1

    if len(seat_matches) == 3:
        break

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")
