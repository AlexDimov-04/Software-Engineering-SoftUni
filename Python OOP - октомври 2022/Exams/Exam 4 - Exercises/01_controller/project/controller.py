class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def __find_player(self, some_type: str):
        for player in self.players:
            if player.name == some_type:
                return player

    def __find_supply(self, supply_type: str):
        return [(pos, s) for pos, s in enumerate(self.supplies) if s.__class__.__name__ == supply_type][-1]

    def __duel_winner(self, p1, p2):
        first_player = p1 if p1.stamina < p2.stamina else p2
        second_player = p1 if first_player == p2 else p2
        iterations = 0

        while iterations <= 2:
            if second_player.stamina - first_player.stamina / 2 <= 0:
                second_player.stamina = 0
                return first_player

            elif first_player.stamina - second_player.stamina / 2 <= 0:
                first_player.stamina = 0
                return second_player

            else:
                second_player.stamina -= first_player.stamina / 2
                first_player.stamina -= second_player.stamina / 2

            iterations += 1

        winner = first_player if second_player.stamina < first_player.stamina else second_player
        return winner

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)

        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player(player_name)

        if sustenance_type not in ['Food', 'Drink'] or player not in self.players:
            return

        if player.stamina >= 100:
            return f"{player_name} have enough stamina."

        if sustenance_type == 'Food':
            if all(sustenance_type != f.__class__.__name__ for f in self.supplies):
                raise Exception("There are no food supplies left!")

        elif sustenance_type == 'Drink':
            if all(sustenance_type != d.__class__.__name__ for d in self.supplies):
                raise Exception("There are no drink supplies left!")

        pos, supply = self.__find_supply(sustenance_type)

        if player.stamina + supply.energy > 100:
            supply.energy = 100 - player.stamina

        player.stamina += supply.energy
        del self.supplies[pos]
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        zero_stamina_messages = []

        for p in self.players:
            if p.stamina == 0:
                zero_stamina_messages.append(f"Player {p.name} does not have enough stamina.")

        if zero_stamina_messages:
            result = ''.join(zero_stamina_messages) if len(zero_stamina_messages) == 1 else \
                '\n'.join(zero_stamina_messages)

            return result

        player1 = self.__find_player(first_player_name)
        player2 = self.__find_player(second_player_name)

        winner = self.__duel_winner(player1, player2)

        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - player.age * 2 < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2

        for p in self.players:
            for supply in ['Food', 'Drink']:
                self.sustain(p.name, supply)

    def __str__(self):
        output = []

        for player in self.players:
            output.append(str(player))

        for supply in self.supplies:
            output.append(supply.details())

        return '\n'.join(output)

# from project.player import Player
# from project.supply.drink import Drink
# from project.supply.food import Food
#
# controller = Controller()
# apple = Food("apple", 22)
# cheese = Food("cheese")
# juice = Drink("orange juice")
# water = Drink("water")
# first_player = Player('Peter', 15)
# second_player = Player('Lilly', 12, 94)
# print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
# print(controller.add_player(first_player, second_player))
# print(controller.duel("Peter", "Lilly"))
# print(controller.add_player(first_player))
# print(controller.sustain("Lilly", "Drink"))
# first_player.stamina = 0
# print(controller.duel("Peter", "Lilly"))
# print(first_player)
# print(second_player)
# controller.next_day()
# print(controller)
