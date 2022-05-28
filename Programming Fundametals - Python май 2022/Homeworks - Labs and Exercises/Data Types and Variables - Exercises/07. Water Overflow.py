n = int(input())
tank_capacity = 255
filled_capacity = 0

for i in range(1, n + 1):
    liters_water = int(input())
    filled_capacity += liters_water

    if filled_capacity > tank_capacity:
        filled_capacity -= liters_water
        print('Insufficient capacity!')
        continue

print(filled_capacity)
