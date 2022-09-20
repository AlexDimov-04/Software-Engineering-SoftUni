from functools import reduce

expression = input().split()
stack = []

for el in expression:
    if el.lstrip('-').isdigit():
        stack.append(el)
    else:
        if el == "*":
            stack = [reduce(lambda x, y: x * y, stack)]
        elif el == "+":
            stack = [reduce(lambda x, y: x + y, stack)]
        elif el == "-":
            stack = [reduce(lambda x, y: x - y, stack)]
        elif el == "/":
            stack = [reduce(lambda x, y: x // y, stack)]

print(*stack)
