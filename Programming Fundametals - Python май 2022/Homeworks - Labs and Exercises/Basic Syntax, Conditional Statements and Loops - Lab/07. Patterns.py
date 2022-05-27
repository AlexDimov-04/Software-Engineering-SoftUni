nums = int(input())

for i in range(1, nums + 1):
    print(i * '*')

for i in range(nums - 1, 0, -1):
    print(i * '*')