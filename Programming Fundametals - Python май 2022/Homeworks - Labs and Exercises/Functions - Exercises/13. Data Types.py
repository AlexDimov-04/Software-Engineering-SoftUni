def data_checker(data_type, input):
    if data_type == "int":
        return input * 2
    elif data_type == "real":
        result = input * 1.5
        return f'{result:.2f}'
    elif data_type == "string":
        return f'${input}$'


data = input()
if data == "int":
    variable = int(input())
elif data == "real":
    variable = float(input())
elif data == "string":
    variable = input()

print(data_checker(data, variable))
