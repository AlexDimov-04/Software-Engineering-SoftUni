n = int(input())
even_set, odd_set = set(), set()

total_sum_name = 0

for num in range(1, n + 1):
    name = input()
    for ch in name:
        total_sum_name += ord(ch)

    total_sum_name //= num
    if total_sum_name % 2 == 0:
        even_set.add(total_sum_name)
    else:
        odd_set.add(total_sum_name)

    total_sum_name = 0

if sum(even_set) == sum(odd_set):
    union = even_set | odd_set
    print(', '.join(str(x) for x in union))
elif sum(odd_set) > sum(even_set):
    diff = odd_set - even_set
    print(', '.join(str(x) for x in diff))
else:
    symmetric_diff = even_set ^ odd_set
    print(', '.join(str(x) for x in symmetric_diff))
