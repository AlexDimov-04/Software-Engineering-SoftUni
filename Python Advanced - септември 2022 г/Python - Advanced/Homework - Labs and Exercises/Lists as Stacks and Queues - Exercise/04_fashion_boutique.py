clothes = list(map(int, input().split()))
capacity = int(input())
rack = capacity
racks_count = 1

while clothes:
    clothing = clothes.pop()

    if clothing <= rack:
        rack -= clothing
    else:
        racks_count += 1
        rack = capacity
        rack -= clothing

print(racks_count)
