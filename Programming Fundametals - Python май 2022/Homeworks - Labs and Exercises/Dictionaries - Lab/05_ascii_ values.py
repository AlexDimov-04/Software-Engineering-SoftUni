chars = input().split(', ')

ascii_dict = {word: ord(word) for word in chars}
print(ascii_dict)