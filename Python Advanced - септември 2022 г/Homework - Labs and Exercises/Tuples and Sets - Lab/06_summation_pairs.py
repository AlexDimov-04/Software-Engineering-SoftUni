numbers = list(map(int, input().split()))
target_num = int(input())

for n1 in numbers:
    second_nums = numbers[1:]
    for n2 in second_nums:
        if n1 + n2 == target_num:
            print(f"{n1} + {n2} = {target_num}")


