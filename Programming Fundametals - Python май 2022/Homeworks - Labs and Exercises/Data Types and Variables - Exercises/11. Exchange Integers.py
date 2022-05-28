int_1 = int(input())
int_2 = int(input())

a = int_1
b = int_2

print('Before:')
print(f'a = {a}')
print(f'b = {b}')

a, b = int_2, int_1

print('After:')
print(f'a = {a}')
print(f'b = {b}')