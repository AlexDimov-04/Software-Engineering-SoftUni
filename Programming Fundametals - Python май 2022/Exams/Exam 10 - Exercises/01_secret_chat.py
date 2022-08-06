concealed_message = input()


def insert_space(idx):
    global concealed_message
    concealed_message = concealed_message[:idx] + ' ' + concealed_message[idx:]
    print(concealed_message)


def reverse(under_string):
    global concealed_message
    if under_string in concealed_message:
        occurrence = concealed_message.find(under_string)
        concealed_message = concealed_message[:occurrence] + concealed_message[occurrence + (len(under_string)):]
        concealed_message += under_string[::-1]
        print(concealed_message)
    else:
        print("error")


def change_all(under_string, replace):
    global concealed_message
    concealed_message = concealed_message.replace(under_string, replace)
    print(concealed_message)


while True:
    command = input()
    if command == "Reveal":
        break

    command = command.split(':|:')
    if command[0] == "InsertSpace":
        index = int(command[1])
        insert_space(index)
    elif command[0] == "Reverse":
        substring = command[1]
        reverse(substring)
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        change_all(substring, replacement)

print(f"You have a new text message: {concealed_message}")
