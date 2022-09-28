n = int(input())
stack = []

for _ in range(n):
    query = input().split()
    if query[0] == '1':
        number = int(query[1])
        stack.append(number)
    elif len(stack) > 0:
        if query[0] == '2':
            stack.pop()
        elif query[0] == '3':
            print(max(stack))
        elif query[0] == '4':
            print(min(stack))

while stack:
    el = stack.pop()
    if stack:
        print(el, end=', ')
    else:
        print(el)
