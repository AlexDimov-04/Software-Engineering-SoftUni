n = int(input())
res_code = set()

for _ in range(n):
    res_code.add(input())

while True:
    guest = input()
    if guest == "END":
        break

    if guest in res_code:
        res_code.discard(guest)

print(len(res_code))
output = sorted(res_code)
print(*output, sep='\n')
