n = int(input())
synonyms = {}

for i in range(n):
    word_one = input()
    word_two = input()

    if word_one not in synonyms:
        synonyms[word_one] = []
        synonyms[word_one].append(word_two)
    else:
        synonyms[word_one].append(word_two)

for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")
