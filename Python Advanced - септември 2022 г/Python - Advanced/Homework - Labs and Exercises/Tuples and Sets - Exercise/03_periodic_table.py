n = int(input())
unique_chemicals = set()

for _ in range(n):
    chemical = input().split()
    for i in chemical:
        unique_chemicals.add(i)

print(*unique_chemicals, sep='\n')
