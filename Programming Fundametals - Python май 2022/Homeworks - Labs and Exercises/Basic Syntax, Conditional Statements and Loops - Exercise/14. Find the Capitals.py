command = input()
index = []

for i in range(len(command)):
    if command[i].isupper():
        index.append(i)
print(index)
