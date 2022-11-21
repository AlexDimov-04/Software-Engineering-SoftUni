n = int(input())
unique_plates = set()

for _ in range(n):
    direction, plate = input().split(', ')

    if direction == "IN":
        unique_plates.add(plate)
    elif direction == "OUT":
        unique_plates.discard(plate)

if unique_plates:
    print(*unique_plates, sep='\n')
else:
    print("Parking Lot is Empty")
