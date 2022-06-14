fire_with_cells = input().split("#")
water = int(input())

removed_values = []
effort = 0
total_fire = 0

for i in fire_with_cells:
    index = i.split(" = ")
    fire_type = index[0]
    cells_value = int(index[1])
    valid = False

    if water < cells_value:
        continue

    if fire_type == "High":
        if 81 <= cells_value <= 125:
            valid = True
    elif fire_type == "Medium":
        if 51 <= cells_value <= 80:
            valid = True
    elif fire_type == "Low":
        if 1 <= cells_value <= 50:
            valid = True

    if valid:
        removed_values.append(cells_value)
        water -= cells_value
        effort += 0.25 * cells_value
        total_fire += cells_value

print('Cells:')
for j in removed_values:
    print(f' - {j}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')

