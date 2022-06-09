combination = input()
combination = combination.lower()
counter = 0

words = ['sand', 'water', 'fish', 'sun']

for i in words:
    if i in combination:
        word_repeat = combination.count(i)
        counter += word_repeat
print(counter)
