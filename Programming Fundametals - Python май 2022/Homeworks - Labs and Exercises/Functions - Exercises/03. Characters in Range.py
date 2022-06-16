def get_chars(char_1, char_2):
    collected_chars = []
    for current_char in range(ord(char_1) + 1, ord(char_2)):
        collected_chars.append(chr(current_char))
    return collected_chars


char_1 = input()
char_2 = input()
result = get_chars(char_1, char_2)
print(' '.join(result))
