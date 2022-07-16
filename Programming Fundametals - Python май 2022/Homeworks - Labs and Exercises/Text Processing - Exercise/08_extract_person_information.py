n = int(input())

for _ in range(n):
    info = input()
    name = info[info.index('@') + 1:info.index("|")]
    age = info[info.index('#') + 1:info.index("*")]
    print(f"{name} is {age} years old.")
