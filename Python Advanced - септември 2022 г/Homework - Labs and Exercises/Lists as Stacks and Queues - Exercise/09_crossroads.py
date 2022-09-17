from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()
passed_cars = 0

crashed = False

while True:
    command = input()
    if command == "END":
        break

    if command == "green":
        if cars:
            current_car = cars.popleft()
            remaining_seconds = green_light - len(current_car)
            while remaining_seconds > 0:
                passed_cars += 1
                if cars:
                    current_car = cars.popleft()
                    remaining_seconds -= len(current_car)
                else:
                    break
            if remaining_seconds == 0:
                passed_cars += 1
            if free_window >= abs(remaining_seconds):
                if remaining_seconds < 0:
                    passed_cars += 1
            else:
                index = free_window + remaining_seconds
                print(f"A crash happened! \n{current_car} was hit at {current_car[index]}.")
                crashed = True
                break
    else:
        cars.append(command)

if not crashed:
    print(f"Everyone is safe. \n{passed_cars} total cars passed the crossroads.")
