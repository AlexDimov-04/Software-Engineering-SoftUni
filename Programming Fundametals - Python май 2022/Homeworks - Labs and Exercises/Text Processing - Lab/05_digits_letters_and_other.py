text = input()
digits = ""
letters = ""
other_symbols = ""

for symbol in text:
    if symbol.isdigit():
        digits += symbol
    elif symbol.isalpha():
        letters += symbol
    else:
        other_symbols += symbol

print(digits)
print(letters)
print(other_symbols)
