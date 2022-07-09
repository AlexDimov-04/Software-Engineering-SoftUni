from collections import defaultdict

words = input().split(' ')
word_count = defaultdict(int)

for word in words:
    word_count[word.lower()] += 1

print(' '.join([word for word, count in word_count.items() if count % 2 != 0]))