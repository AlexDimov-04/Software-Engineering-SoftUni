from collections import Counter


def numbers_searching(*args):
    missing_num = 0
    counter = Counter(args)
    numbers_list = sorted(set(args))
    duplicated_nums = []

    for n in range(min(args), max(args) + 1):
        if n not in numbers_list:
            missing_num = n
            break

    for num, count in counter.items():
        if count > 1:
            duplicated_nums.append(num)

    return [missing_num, sorted(duplicated_nums)]
