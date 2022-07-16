text = input()

for index, char in enumerate(text):
    if char == ":":
        print(char + text[index + 1])
        