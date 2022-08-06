import re

text_string = input()

pattern = r'(\=|\/)([A-Z][A-Za-z]{2,})\1'

result = re.finditer(pattern, text_string)
destination_list = []
travel_points = 0


for el in result:
    destination_list.append(el.group(2))
for destination in destination_list:
    travel_points += len(destination)

print(f"Destinations: {', '.join([str(x) for x in destination_list])}")
print(f"Travel Points: {travel_points}")
