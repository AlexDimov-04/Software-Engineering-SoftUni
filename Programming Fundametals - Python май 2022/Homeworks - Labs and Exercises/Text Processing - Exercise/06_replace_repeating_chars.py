symbols = input()

for index, letter in enumerate(range(len(symbols) - 1), 1):
    if symbols[letter] != symbols[index]:
        print(symbols[letter], end='')

print(symbols[-1])
