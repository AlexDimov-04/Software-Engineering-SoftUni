def shopping_list(budget, **kwargs):
    result = ''
    products_dict = {}

    if budget < 100:
        return 'You do not have enough budget.'
    else:
        for product, values in kwargs.items():
            price, quantity = values

            if price * quantity <= budget:
                result += f"You bought {product} for {price * quantity:.2f} leva." + '\n'
                budget -= price * quantity

                if product not in products_dict:
                    products_dict[product] = quantity
                else:
                    products_dict[product] += quantity

            if len(products_dict) == 5:
                return result

    return result


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
