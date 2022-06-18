version = [int(num) for num in input().split('.')]
version[-1] += 1

for current_index in range(len(version) - 1, -1, -1):
    if version[current_index] > 9:
        version[current_index] = 0
        version[current_index - 1] += 1
print('.'.join(str(num) for num in version))

# 2 way
version = input()
version = version.replace('.', '')
print(int(version) + 1)
