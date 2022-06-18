message = input().split()
deciphered_message = []

for word in message:
    characters = [char for char in word if not char.isdigit()]
    nums = [digit for digit in word if digit.isdigit()]
    ascii_char = [chr(int(''.join(nums)))]
    current_word = ascii_char + characters
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    deciphered_message.append(''.join(current_word))
print(' '.join(deciphered_message))

