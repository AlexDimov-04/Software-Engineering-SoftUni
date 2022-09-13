string = input()
stack = []

for index, char in enumerate(string):
    if char == "(":
        stack.append(index)
    elif char == ")":
        opened_bracket_index = stack.pop()
        expression = string[opened_bracket_index:index + 1]

        print(expression)
