num_orders = int(input())
total = 0
total_sum = 0

for i in range(1, num_orders + 1):
    price_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_capsule < 0.01 or price_capsule > 100.00:
        continue
    if days < 1 or days > 31:
        continue
    if capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    total = price_capsule * days * capsules_per_day
    total_sum += total
    print(f"The price for the coffee is: ${total:.2f}")

print(f"Total: ${total_sum:.2f}")
