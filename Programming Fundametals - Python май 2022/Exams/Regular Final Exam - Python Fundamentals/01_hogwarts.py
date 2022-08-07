spell = input()


def abjuration():
    global spell
    spell = spell.upper()
    print(spell)


def necromancy():
    global spell
    spell = spell.lower()
    print(spell)


def illusion(index, letter):
    global spell
    if index in range(len(spell)):
        spell = spell.replace(spell[index], letter, 1)
        print("Done!")
    else:
        print("The spell was too weak.")


def divination(substring_1, substring_2):
    global spell
    if substring_1 in spell:
        spell = spell.replace(substring_1, substring_2)
        print(spell)


def alteration(substring):
    global spell
    if substring in spell:
        spell = spell.replace(substring, "")
        print(spell)


while True:
    command = input()
    if command == "Abracadabra":
        break

    command = command.split(' ')
    if command[0] == "Abjuration":
        abjuration()
    elif command[0] == "Necromancy":
        necromancy()
    elif command[0] == "Illusion":
        index = int(command[1])
        letter = command[2]
        illusion(index, letter)
    elif command[0] == "Divination":
        first_substring = command[1]
        second_substring = command[2]
        divination(first_substring, second_substring)
    elif command[0] == "Alteration":
        subs = command[1]
        alteration(subs)
    else:
        print("The spell did not work!")