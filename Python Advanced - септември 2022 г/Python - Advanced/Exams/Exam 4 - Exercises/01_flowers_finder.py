from collections import deque

vowels = deque(input().split())
consonants = input().split()
words = ['rose', 'tulip', 'lotus', 'daffodil']
word = ''
found = False
count_founded = 0

while True:
    if vowels and consonants:
        vowel = vowels.popleft()
        consonant = consonants.pop()
    else:
        break

    word += vowel + consonant

    for current_word in words:
        count_founded = 0
        for ch in range(len(current_word)):
            if current_word[ch] in word:
                count_founded += 1
                if count_founded == len(current_word):
                    found = True
                    print(f"Word found: {current_word}")
                    break
        if found:
            break

    if found:
        break

if not found:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
