from unittest import TestCase, main
from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):
    def setUp(self):
        self.cart = ShoppingCart('Lidl', 10_000)
        self.other_cart = ShoppingCart('Billa', 20_000)

    def test_correct_initialization(self):
        self.assertEqual(self.cart.shop_name, 'Lidl')
        self.assertEqual(self.cart.budget, 10_000)
        self.assertEqual(self.cart.products, {})

    def test_shop_name_if_non_valid(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = 'lidl'

        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_too_expensive_product_price_declined_sum(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart('mp3', 100)

        self.assertEqual(str(ve.exception), "Product mp3 cost too much!")

    def test_enough_price_to_buy_product(self):
        result = self.cart.add_to_cart('mp3', 90)

        self.assertEqual(self.cart.products['mp3'], 90)
        self.assertEqual(result, "mp3 product was successfully added to the cart!")

    def test_delete_product_if_it_is_already_in_cart(self):
        self.cart.products = {'mp3': 2, 'mp5': 5}
        result = self.cart.remove_from_cart('mp3')

        self.assertEqual(len(self.cart.products), 1)
        self.assertEqual(result, "Product mp3 was successfully removed from the cart!")

    def test_delete_product_if_product_is_not_in_the_cart(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart('mp4')

        self.assertEqual(str(ve.exception), "No product with name mp4 in the cart!")

    def test_add_product_to_another_cart(self):
        self.cart.products = {'disk': 50}
        self.other_cart.products = {'gpu': 200}
        merged_shops_data = self.cart + self.other_cart

        self.assertEqual(merged_shops_data.shop_name, 'LidlBilla')
        self.assertEqual(merged_shops_data.budget, 30_000)
        self.assertEqual(merged_shops_data.products, {'disk': 50, 'gpu': 200})

    def test_to_buy_products_if_the_sum_is_enough(self):
        self.cart.products = {'TV': 500, 'Sofa': 200}
        total_sum = sum(self.cart.products.values())

        self.assertEqual(self.cart.buy_products(), f'Products were successfully bought! Total cost: {total_sum:.2f}lv.')

    def test_to_buy_products_if_the_sum_is_not_enough(self):
        self.cart.products = {'Tesla': 50_000}
        total_sum = sum(self.cart.products.values())

        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()

        self.assertEqual(str(ve.exception),
                         f"Not enough money to buy the products! Over budget with {total_sum - self.cart.budget:.2f}lv!")


if __name__ == '__main__':
    main()
