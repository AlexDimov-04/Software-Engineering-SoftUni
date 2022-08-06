import re

text = input()

search_pattern = r"\b_([A-Za-z0-9]+)\b"

result = re.findall(search_pattern, text)

print(','.join(result))
