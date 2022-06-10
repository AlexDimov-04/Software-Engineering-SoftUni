gifts = input().split()
command = input()

while command != 'No Money':
    command = command.split()
    if 'OutOfStock' in command:
        for i in range(len(gifts)):
            if command[1] in gifts[i]:
                gifts[i] = 'None'
    elif 'Required' in command:
        for i in range(len(gifts)):
            if i == int(command[2]):
                gifts[i] = command[1]
                break
    elif 'JustInCase' in command:
        gifts[-1] = command[1]
    command = input()
while 'None' in gifts:
    gifts.remove('None')
for i in gifts:
    print(i, end=' ')



