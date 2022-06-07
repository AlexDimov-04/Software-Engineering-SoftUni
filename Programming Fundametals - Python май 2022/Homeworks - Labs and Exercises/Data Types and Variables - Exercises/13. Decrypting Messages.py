key = int(input())
num_lines = int(input())
message = ''

for i in range(num_lines):
    letter = input()
    dec = ord(letter)
    operation = dec + key
    operation_2 = chr(operation)
    message += operation_2

print(message)

