budget = float(input())
price_kg_flour = float(input())

loaves = 0
colored_eggs = 0

eggs_pack_price = 0.75 * price_kg_flour
liter_milk_price = 1.25 * price_kg_flour

bread_price = price_kg_flour + eggs_pack_price + liter_milk_price * 0.25

while budget >= bread_price:
    loaves += 1
    colored_eggs += 3
    budget -= bread_price

    if loaves % 3 == 0:
        colored_eggs -= (loaves - 2)

print(f'You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
