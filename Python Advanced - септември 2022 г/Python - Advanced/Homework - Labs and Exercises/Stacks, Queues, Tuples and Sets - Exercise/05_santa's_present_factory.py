from collections import deque

toys_dict = {
    "Doll": {'magic': 150, 'crafted': 0},
    "Wooden train": {'magic': 250, 'crafted': 0},
    "Teddy bear": {'magic': 300, 'crafted': 0},
    "Bicycle": {'magic': 400, 'crafted': 0}
}

box_materials = list(map(int, input().split()))  # stack
magic_values = deque(map(int, input().split()))  # queue
total_magic_level = 0

while box_materials and magic_values:
    if box_materials[-1] * magic_values[0] == toys_dict['Doll']['magic']:
        toys_dict['Doll']['crafted'] += 1
        box_materials.pop()
        magic_values.popleft()
    elif box_materials[-1] * magic_values[0] == toys_dict['Wooden train']['magic']:
        toys_dict['Wooden train']['crafted'] += 1
        box_materials.pop()
        magic_values.popleft()
    elif box_materials[-1] * magic_values[0] == toys_dict['Teddy bear']['magic']:
        toys_dict['Teddy bear']['crafted'] += 1
        box_materials.pop()
        magic_values.popleft()
    elif box_materials[-1] * magic_values[0] == toys_dict['Bicycle']['magic']:
        toys_dict['Bicycle']['crafted'] += 1
        box_materials.pop()
        magic_values.popleft()
    else:
        product = box_materials[-1] * magic_values[0]
        if product < 0:
            box_materials.append(box_materials.pop() + magic_values.popleft())
        elif product > 0:
            magic_values.popleft()
            box_materials[-1] += 15
        else:
            if box_materials[-1] == 0 and magic_values[0] == 0:
                box_materials.pop()
                magic_values.popleft()
                continue
            elif box_materials[-1] == 0:
                box_materials.pop()
                continue
            elif magic_values[0] == 0:
                magic_values.popleft()
                continue

if toys_dict['Doll']['crafted'] > 0 and toys_dict['Wooden train']['crafted'] > 0 or \
        toys_dict['Teddy bear']['crafted'] > 0 and toys_dict['Bicycle']['crafted'] > 0:
    print("The presents are crafted! Merry Christmas!")
    if box_materials:
        print(f"Materials left: {', '.join(str(x) for x in box_materials[::-1])}")
    if magic_values:
        print(f"Magic left: {', '.join(str(x) for x in magic_values)}")
else:
    print("No presents this Christmas!")
    if box_materials:
        print(f"Materials left: {', '.join(str(x) for x in box_materials[::-1])}")
    if magic_values:
        print(f"Magic left: {', '.join(str(x) for x in magic_values)}")

for toy in sorted(toys_dict):
    if toys_dict[toy]['crafted'] > 0:
        print(f"{toy}: {toys_dict[toy]['crafted']}")

