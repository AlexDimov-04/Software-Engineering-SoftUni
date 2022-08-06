password = input()

while True:
    command = input().split(' ')
    if command[0] == "Done":
        print(f"Your password is: {password}")
        break

    elif command[0] == "TakeOdd":
        password = ''.join([password[i] for i in range(len(password)) if i % 2 != 0])
        print(password)
        
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        password = password[:index] + password[index + length:]
        print(password)

    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]

        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
