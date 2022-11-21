def reverse_text(string):
    string = string[::-1]

    for idx in range(len(string)):
        yield string[idx]


for char in reverse_text("step"):
    print(char, end='')
