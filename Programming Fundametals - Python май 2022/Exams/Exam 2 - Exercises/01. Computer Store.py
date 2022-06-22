total_price = 0
final_price = 0
taxes = 0

while True:
    client = input()
    if client == 'special' or client == 'regular':
        break
    price_without_tax = float(client)

    if price_without_tax < 0:
        print('Invalid price!')
        continue

    total_price += price_without_tax

if total_price == 0:
    print('Invalid order!')
else:
    taxes = total_price * 0.2
    final_price = total_price + taxes

if client == 'special':
    receipt = final_price - (0.1 * final_price)
    print("Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          "-----------\n"
          f"Total price: {receipt:.2f}$\n")

elif client == 'regular' and total_price > 0:
    print("Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          "-----------\n"
          f"Total price: {final_price:.2f}$\n")


