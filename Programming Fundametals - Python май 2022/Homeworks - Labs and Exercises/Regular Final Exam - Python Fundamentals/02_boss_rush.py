import re

number = int(input())

for _ in range(number):
    data = input()

    pattern = r'(\|)([A-Z]{4,})\1\:(\#)([A-Za-z]+\s[A-Za-z]+)\3'
    result = re.match(pattern, data)

    if result:
        print(f"{result.group(2)}, The {result.group(4)}")
        print(f">> Strength: {len(result.group(2))}")
        print(f">> Armor: {len(result.group(4))}")
    else:
        print("Access denied!")
