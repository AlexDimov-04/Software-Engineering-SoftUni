from project.client import Client
from project.meals.meal import Meal
from project.meals.starter import Starter
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")

        current_client = Client(client_phone_number)
        self.clients_list.append(current_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if type(meal).__name__ in ['Starter', 'MainDish', 'Dessert']:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        menu_details = []

        for meal in self.menu:
            menu_details.append(meal.details())

        return '\n'.join(menu_details)

    def __check_if_meal_is_in_menu(self, meal_name):
        for meal in self.menu:
            if meal.name == meal_name:
                return True

    def __find_meal(self, meal_name):
        for meal in self.menu:
            if meal.name == meal_name:
                return meal

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        for client in self.clients_list:
            if client.phone_number != client_phone_number:
                self.register_client(client_phone_number)

        current_client = None
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                current_client = client
                break

        current_shopping_cart = []
        current_bill = 0

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            if not self.__check_if_meal_is_in_menu(meal_name):
                raise Exception(f"{meal_name} is not on the menu!")

            current_meal = self.__find_meal(meal_name)
            if current_meal.quantity < meal_quantity:
                raise Exception(f"Not enough quantity of {type(current_meal).__name__}: {current_meal.name}!")

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            current_meal = self.__find_meal(meal_name)
            current_client.shopping_cart.append(current_meal)
            current_client.bill += current_meal.price * meal_quantity
            current_meal.quantity -= meal_quantity
            current_client.ordered_quantities[current_meal.name] = meal_quantity

        ordered_meal_names = []
        for ordered_meal in current_client.shopping_cart:
            ordered_meal_names.append(ordered_meal.name)

        return f"Client {client_phone_number} successfully ordered {', '.join(ordered_meal_names)} for " \
               f"{current_client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        current_client = None
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                current_client = client
                break

        if not current_client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal_name, meal_quantity in current_client.ordered_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity += meal_quantity
        current_client.shopping_cart = []
        current_client.ordered_quantities = {}
        current_client.bill = 0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        current_client = None
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                current_client = client
                break

        if not current_client.shopping_cart:
            raise Exception("There are no ordered meals!")

        bill_paid = current_client.bill
        current_client.shopping_cart = []
        current_client.ordered_quantities = {}

        current_client.bill = 0
        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {bill_paid:.2f} was successfully paid " \
               f"for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."


food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
print(food_orders_app.add_meals_to_menu(
    french_toast, hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets))
print(food_orders_app.show_menu())
food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
additional_food = {"Risotto with Wild Mushrooms": 2,
                   "Tortilla with Beef and Pork": 2}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
print(food_orders_app.finish_order("0899999999"))
print(food_orders_app)
