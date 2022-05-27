quantity = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

price = 0
points = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 10 == 0:
        points -= 20
        price += tree_skirt + tree_lights + tree_garlands
        if day == days:
            points -= 30
    if day % 5 == 0:
        price += tree_lights * quantity
        points += 17
    if day % 15 == 0:
        points += 30
    if day % 3 == 0:
        points += 13
        price += (tree_skirt + tree_garlands) * quantity
    if day % 2 == 0:
        points += 5
        price += ornament_set * quantity

print(f"Total cost: {price}")
print(f"Total spirit: {points}")