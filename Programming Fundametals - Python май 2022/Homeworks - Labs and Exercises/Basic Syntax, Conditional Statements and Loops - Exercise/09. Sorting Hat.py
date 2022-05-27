name = input()

while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    for chars in range(len(name)):
        chars += 1
        if chars != len(name):
            continue
        if chars < 5:
            print(f"{name} goes to Gryffindor.")
        elif chars == 5:
            print(f"{name} goes to Slytherin.")
        elif chars == 6:
            print(f"{name} goes to Ravenclaw.")
        else:
            print(f"{name} goes to Hufflepuff.")
    name = input()

if name == "Welcome!":
    print("Welcome to Hogwarts.")