from collections import Counter

text = input()
lst = []

for ch in text:
    lst += ch

counter = Counter(lst)

for char, rep in sorted(counter.items()):
    print(f"{char}: {rep} time/s")
