def move_zero(num_list):
    a = [0 for x in range(num_list.count(0))]
    b = [x for x in num_list if x != 0]
    b.extend(a)
    return b


nums = list(map(int, input().split(', ')))
print(move_zero(nums))
