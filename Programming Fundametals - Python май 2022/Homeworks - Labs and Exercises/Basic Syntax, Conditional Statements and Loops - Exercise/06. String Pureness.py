n = int(input())
current_symbol = ''

for i in range(1, n + 1):
    string = input()
    if ',' in string or '.' in string or '_' in string:
        print(f"{string} is not pure!")
    else:
        print(f'{string} is pure.')
