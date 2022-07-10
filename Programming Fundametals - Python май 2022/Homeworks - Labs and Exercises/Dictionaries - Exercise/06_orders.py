products_quantity = {}
products_prices = {}

while True:
    command = input()
    if command == "buy":
        break

    command = command.split()
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if product not in products_quantity.keys():
        products_quantity[product] = 0
        products_prices[product] = 0.0
    products_quantity[product] += quantity
    products_prices[product] = price

for key, value in products_quantity.items():
    total_price = value * products_prices[key]
    print(f"{key} -> {total_price:.2f}")
