num = int(input())

# recursive method
def draw_figure(n):
    if n <= 0:
        return
    
    print('*' * n)
    draw_figure(n - 1)
    print('#' * n)

draw_figure(num)

# iterative method
"""
for i in range(n, 0, -1):
    print('*' * i)

for j in range(1, n + 1):
    print('#' * j)
"""
