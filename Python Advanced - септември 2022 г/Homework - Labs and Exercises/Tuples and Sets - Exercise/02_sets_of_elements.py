n, m = input().split()
set_1, set_2 = set(), set()

for _ in range(int(n)):
    num = int(input())
    set_1.add(num)

for _ in range(int(m)):
    num = int(input())
    set_2.add(num)

unique_elements = set_1 & set_2
print(*unique_elements, sep='\n')
