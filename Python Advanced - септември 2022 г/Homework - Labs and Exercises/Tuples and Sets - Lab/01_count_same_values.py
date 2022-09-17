from collections import Counter

numbers = tuple(map(float, input().split()))
counter = Counter(numbers)

for num, rep in counter.items():
    print(f"{num:.1f} - {rep} times")
