from collections import defaultdict

letters = defaultdict(int)
symbols = ''.join(x for x in input().split())

for letter in symbols:
    letters[letter] += 1

for key, value in letters.items():
    print(f"{key} -> {value}")
