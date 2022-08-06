import re

search_pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)\!(\d+)"

total_cost = 0
valid_furniture = []

command = input()

while command != "Purchase":
    match = re.search(search_pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        valid_furniture.append(furniture)
        total_cost += int(quantity) * float(price)

    command = input()

print("Bought furniture:")
for furniture in valid_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")
