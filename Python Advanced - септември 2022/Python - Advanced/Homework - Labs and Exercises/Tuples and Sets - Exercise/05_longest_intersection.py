n = int(input())
set_1 = set()
set_2 = set()
list_intersections = []
max_length = 0
longest_intersection = {}

for _ in range(n):
    range1, range2 = input().split('-')
    start1, end1 = list(map(int, range1.split(',')))
    start2, end2 = list(map(int, range2.split(',')))

    for i in range(start1, end1 + 1):
        set_1.add(i)

    for i in range(start2, end2 + 1):
        set_2.add(i)

    intersection = set_1 & set_2
    list_intersections.append(intersection)

    set_1 = set()
    set_2 = set()

for inter in list_intersections:
    if len(inter) > max_length:
        max_length = len(inter)
        longest_intersection = inter

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length {max_length}")
