n = int(input())
letters_sum = 0

for i in range(1, n + 1):
    char = input()
    letters_sum += ord(char)

print(f'The sum equals: {letters_sum}')
