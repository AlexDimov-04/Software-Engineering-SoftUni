command = ""
coffee = 0

while command != "END":
    command = input()
    if command == "coding" or command == "CODING":
        if command.islower():
            coffee += 1
        elif command.isupper():
            coffee += 2
    elif command == "dog" or command == "DOG" or command == "cat" or command == "CAT":
        if command.islower():
            coffee += 1
        elif command.isupper():
            coffee += 2
    elif command == "movie" or command == "MOVIE":
        if command.islower():
            coffee += 1
        elif command.isupper():
            coffee += 2
    else:
        continue


if coffee > 5:
    print("You need extra sleep")
else:
    print(f"{coffee}") 