def shopping_cart(*args):
    products_dict = {}
    result = ''
    for products in args:
        if products == "Stop":
            if not products_dict:
                return "No products in the cart!"
            for meal, products_pack in sorted(products_dict.items(), key=lambda x: (-len(x[1]), x[0], x[1])):
                result += f"{meal}:" + '\n'
                for product in sorted(products_pack):
                    result += f" - {product}" + '\n'

            for meal in sorted(["Pizza", "Soup", "Dessert"]):
                if meal not in products_dict:
                    result += f"{meal}:" + '\n'
            break

        meal, product = products

        if meal == "Pizza":
            if meal not in products_dict:
                products_dict[meal] = {product}
            else:
                if len(products_dict[meal]) < 4:
                    products_dict[meal].add(product)

        elif meal == "Soup":
            if meal not in products_dict:
                products_dict[meal] = {product}
            else:
                if len(products_dict[meal]) < 3:
                    products_dict[meal].add(product)

        elif meal == "Dessert":
            if meal not in products_dict:
                products_dict[meal] = {product}
            else:
                if len(products_dict[meal]) < 2:
                    products_dict[meal].add(product)

    return result
