def draw_rhombus(n, ch):
    print(' ' * (n - ch), end='')
    print('* ' * ch)


n = int(input())

for i in range(1, n + 1):
    draw_rhombus(n, i)

for j in range(n - 1, -1, -1):
    draw_rhombus(n, j)
