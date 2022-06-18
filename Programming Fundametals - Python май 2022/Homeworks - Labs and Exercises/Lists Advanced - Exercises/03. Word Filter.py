text = input().split(' ')
result = [word for word in text if len(word) % 2 == 0]
for current_word in result:
    print(current_word)
