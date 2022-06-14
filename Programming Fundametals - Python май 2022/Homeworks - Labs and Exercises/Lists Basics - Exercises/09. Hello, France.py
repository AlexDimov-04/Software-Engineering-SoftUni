items_prices = input().split('|')
budget = int(input())

train_ticket = 150
clothes_max_price = 50
shoes_max_price = 35
accessories_max_price = 20.50
income = 0
bought_items_prices = []

for current_item in items_prices:
    index = current_item.split('->')
    item = index[0]
    price = float(index[1])

    if budget < price:
        continue

    if item == 'Clothes' and price <= clothes_max_price:
        budget -= price
        bought_items_prices.append(price)
    elif item == 'Shoes' and price <= shoes_max_price:
        budget -= price
        bought_items_prices.append(price)
    elif item == 'Accessories' and price <= accessories_max_price:
        budget -= price
        bought_items_prices.append(price)
    else:
        continue

for current_price in bought_items_prices:
    increased_value = current_price + (0.4 * current_price)
    income += increased_value
    print(f'{increased_value:.2f}', end=' ')

print('')
profit = income - sum(bought_items_prices)
budget += income
print(f'Profit: {profit:.2f}')

if budget >= train_ticket:
    print('Hello, France!')
else:
    print('Not enough money.')
