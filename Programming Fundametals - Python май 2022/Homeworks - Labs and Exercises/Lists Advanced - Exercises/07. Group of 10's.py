number_list = [int(n) for n in input().split(", ")]

for group in range(1, 11):
    check_list = []
    if len(number_list) != 0:
        [check_list.append(x) for x in number_list if x <= (group * 10)]
        [number_list.remove(i) for i in check_list]
        print(f"Group of {group * 10}'s: {check_list}")

