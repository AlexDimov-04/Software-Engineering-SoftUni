import os

command = input().split('-')

while command[0] != 'End':
    file_name = command[1]

    if command[0] == "Create":
        with open(f'./{file_name}', 'w') as created_file:
            created_file.close()

    elif command[0] == "Add":
        content = command[2]
        with open(f'./{file_name}', 'a') as added_file:
            added_file.write(f"{content}\n")

    elif command[0] == "Replace":
        old_str = command[2]
        new_str = command[3]
        try:
            with open(f'./{file_name}', 'r') as replacing_file:
                text = replacing_file.readlines()

                replacing_file = open(f'./{file_name}', 'w')

                for line in range(len(text)):
                    text[line] = text[line].replace(old_str, new_str)

                replacing_file.write(''.join(text))
                replacing_file.close()
        except FileNotFoundError:
            print('An error occurred')

    elif command[0] == "Delete":
        try:
            os.remove(f'./{file_name}')
        except FileNotFoundError:
            print('An error occurred')

    else:
        break

    command = input().split('-')
