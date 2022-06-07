num_lines = int(input())
opened_brackets = 0
closed_brackets = 0
counter = 0

for i in range(num_lines):
    command = input()

    if command == '(':
        opened_brackets += 1
    elif command == ')':
        closed_brackets += 1

if opened_brackets == closed_brackets:
    print('BALANCED')
else:
    print('UNBALANCED')
