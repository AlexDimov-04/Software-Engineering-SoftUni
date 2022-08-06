message = input()


def move(number):
    global message
    message = message[number:] + message[:number]


def insert(idx, symbol):
    global message
    message = message[:idx] + symbol + message[idx:]


def change_all(letter_one, letter_two):
    global message
    message = message.replace(letter_one, letter_two)


while True:
    command = input()
    if command == "Decode":
        break

    command = command.split('|')

    if command[0] == "Move":
        number_of_letters = int(command[1])
        move(number_of_letters)
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        insert(index, value)
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        change_all(substring, replacement)

print(f"The decrypted message is: {message}")
