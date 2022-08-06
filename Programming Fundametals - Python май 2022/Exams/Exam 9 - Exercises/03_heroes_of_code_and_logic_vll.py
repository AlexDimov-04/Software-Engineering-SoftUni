def create_heroes(heroes, number):
    for _ in range(number):
        data = input().split(' ')
        hero_name = data[0]
        hp = int(data[1])
        mp = int(data[2])

        heroes[hero_name] = {'HP': hp, 'MP': mp}

    return heroes


def additional_heroes_data(heroes):

    while True:
        command = input().split(' - ')
        if command[0] == "End":
            break

        elif command[0] == "CastSpell":
            hero_name = command[1]
            mp_needed = int(command[2])
            spell_name = command[3]
            if heroes[hero_name]['MP'] >= mp_needed:
                heroes[hero_name]['MP'] -= mp_needed
                print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif command[0] == "TakeDamage":
            hero_name = command[1]
            damage = int(command[2])
            attacker = command[3]
            heroes[hero_name]['HP'] -= damage
            if heroes[hero_name]['HP'] > 0:
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
            else:
                del heroes[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")

        elif command[0] == "Recharge":
            hero_name = command[1]
            amount = int(command[2])
            if heroes[hero_name]['MP'] + amount > 200:
                amount = 200 - heroes[hero_name]['MP']
                heroes[hero_name]['MP'] = 200
            else:
                heroes[hero_name]['MP'] += amount
            print(f"{hero_name} recharged for {amount} MP!")

        elif command[0] == "Heal":
            hero_name = command[1]
            amount = int(command[2])
            if heroes[hero_name]['HP'] + amount > 100:
                amount = 100 - heroes[hero_name]['HP']
                heroes[hero_name]['HP'] = 100
            else:
                heroes[hero_name]['HP'] += amount
            print(f"{hero_name} healed for {amount} HP!")

    return heroes


def final_result(heroes):
    for hero, stats in heroes.items():
        print(hero)
        for type_health, num_health in stats.items():
            print(f" {type_health}: {num_health}")


def heroes_of_code_and_logic(number):
    heroes = {}

    create_heroes(heroes, number)
    additional_heroes_data(heroes)
    final_result(heroes)


n = int(input())
heroes_of_code_and_logic(n)
