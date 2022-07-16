first_char, second_char, string = input(), input(), input()
total_sum = 0

for character in string:
    if ord(first_char) < ord(character) < ord(second_char):
        total_sum += ord(character)

print(total_sum)
