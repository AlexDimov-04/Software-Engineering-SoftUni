parentheses = input()
brackets = []
balanced = False

for el in parentheses:
    if el in '({[':
        brackets.append(el)
    elif el in ')}]' and brackets:
        last_el = brackets.pop()
        if last_el + el in '(){}[]':
            balanced = True
        else:
            balanced = False
            break
    else:
        balanced = False
        break

if balanced and not brackets:
    print('YES')
else:
    print('NO')
