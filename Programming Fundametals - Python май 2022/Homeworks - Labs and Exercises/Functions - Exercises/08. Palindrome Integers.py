numbers = input().split(", ")
num_backwards = ""
for num in numbers:
    num_backwards = num[::-1]
    if num == num_backwards:
        print('True')
    else:
        print('False')

#2 way
print('\n'.join([str(n == n[::-1]) for n in input().split(", ")]))
