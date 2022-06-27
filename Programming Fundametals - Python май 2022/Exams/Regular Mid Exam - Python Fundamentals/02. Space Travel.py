travel_route = input().split('||')
starting_amount_fuel = int(input())
starting_amount_ammunition = int(input())

for command in travel_route:
    separation = command.split(' ')

    if separation[0] == "Travel":
        light_years = int(separation[1])
        if starting_amount_fuel >= light_years:
            starting_amount_fuel -= light_years
            print(f"The spaceship travelled {light_years} light-years.")
        else:
            print(f"Mission failed.")
            break

    elif separation[0] == "Enemy":
        enemy_armour = int(separation[1])
        if starting_amount_ammunition >= enemy_armour:
            starting_amount_ammunition -= enemy_armour
            print(f"An enemy with {enemy_armour} armour is defeated.")
        else:
            for enemy_point in range(1, enemy_armour + 1):
                starting_amount_fuel -= 2
            if starting_amount_fuel >= enemy_armour:
                print(f"An enemy with {enemy_armour} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break

    elif separation[0] == "Repair":
        num_ammunition_and_fuel_added = int(separation[1])
        starting_amount_fuel += num_ammunition_and_fuel_added
        starting_amount_ammunition += num_ammunition_and_fuel_added * 2
        print(f"Ammunitions added: {num_ammunition_and_fuel_added * 2}.")
        print(f"Fuel added: {num_ammunition_and_fuel_added}.")

    elif separation[0] == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
