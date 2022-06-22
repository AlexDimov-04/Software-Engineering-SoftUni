quantity_food_kg = float(input()) * 1000
quantity_hay_kg = float(input()) * 1000
quantity_cover_kg = float(input()) * 1000
guinea_pig_weight = float(input()) * 1000

for day in range(1, 31):
    quantity_food_kg -= 300

    if quantity_food_kg <= 0 or quantity_cover_kg <= 0 or quantity_hay_kg <= 0:
        print('Merry must go to the pet store!')
        break

    if day % 2 == 0:
        hay = quantity_food_kg * 0.05
        quantity_hay_kg -= hay

    if day % 3 == 0:
        cover = 1/3 * guinea_pig_weight
        quantity_cover_kg -= cover

else:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food_kg / 1000:.2f}, Hay: {quantity_hay_kg / 1000:.2f}, Cover: {quantity_cover_kg / 1000:.2f}.")

