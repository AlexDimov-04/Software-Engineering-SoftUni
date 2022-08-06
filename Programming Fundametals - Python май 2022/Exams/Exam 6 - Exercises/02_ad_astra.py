import re

text_string = input()

pattern = r'(#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1'

result = re.finditer(pattern, text_string)
list_products = []
total_sum = 0

for match in result:
    list_products.append([match.group(2), match.group(3), match.group(4)])
    total_sum += int(match.group(4))

days = total_sum // 2000

print(f"You have food to last you for: {days} days!")

for element in list_products:
    print(f"Item: {element[0]}, Best before: {element[1]}, Nutrition: {element[2]}")
