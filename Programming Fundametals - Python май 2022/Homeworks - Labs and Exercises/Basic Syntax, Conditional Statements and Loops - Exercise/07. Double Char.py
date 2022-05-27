string = ''

while string != 'End':
    string = input()
    if string == "End":
        break
    if string == "SoftUni":
        continue
    for i in range(len(string)):
        print(string[i] * 2, end='')
    print()


