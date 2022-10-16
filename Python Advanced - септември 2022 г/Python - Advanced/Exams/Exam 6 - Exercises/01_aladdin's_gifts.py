from collections import deque

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))
counter = 0

items_dict = {'Gemstone': 0, 'Porcelain Sculpture': 0, 'Gold': 0, 'Diamond Jewellery': 0}

while materials and magic:
    total_sum = materials[-1] + magic[0]
    material = materials[-1]
    magic_unit = magic[0]

    while True:
        if 100 <= total_sum <= 499:
            if 100 <= total_sum <= 199:
                items_dict['Gemstone'] += 1

            elif 200 <= total_sum <= 299:
                items_dict['Porcelain Sculpture'] += 1

            elif 300 <= total_sum <= 399:
                items_dict['Gold'] += 1

            elif 400 <= total_sum <= 499:
                items_dict['Diamond Jewellery'] += 1

            counter = 0
            materials.pop()
            magic.popleft()
            break

        else:
            if total_sum < 100:
                counter += 1
                if counter % 2 == 0:
                    counter = 0
                    materials.pop()
                    magic.popleft()
                    break
                if total_sum % 2 == 0:
                    total_sum = material * 2 + magic_unit * 3
                else:
                    if counter % 2 == 0:
                        counter = 0
                        materials.pop()
                        magic.popleft()
                        break
                    total_sum *= 2

            elif total_sum > 499:
                counter += 1
                if counter % 2 == 0:
                    counter = 0
                    materials.pop()
                    magic.popleft()
                    break
                total_sum //= 2

if items_dict['Gemstone'] and items_dict['Porcelain Sculpture'] or items_dict['Gold'] and items_dict[
    'Diamond Jewellery']:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for material, count in sorted(items_dict.items()):
    if count > 0:
        print(f"{material}: {count}")
