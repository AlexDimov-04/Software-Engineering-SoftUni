char_start = int(input())
char_end = int(input())

for i in range(char_start, char_end + 1):
    print(f'{chr(i)} ', end='')
