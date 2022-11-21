symbols = ["-", ",", ".", "!", "?"]

with open('text.txt', 'r') as file:
    text = file.readlines()

for row in range(0, len(text), 2):
    for symbol in symbols:
        text[row] = text[row].replace(symbol, '@')

    print(*text[row].split()[::-1])
