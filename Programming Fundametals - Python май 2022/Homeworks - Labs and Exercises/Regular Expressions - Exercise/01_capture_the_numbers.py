import re

search_pattern = r"\d+"

string = input()
while True:
    if string:
        match = re.findall(search_pattern, string)
        if match:
            print(*match, end=' ')
        string = input()
    else:
        break
