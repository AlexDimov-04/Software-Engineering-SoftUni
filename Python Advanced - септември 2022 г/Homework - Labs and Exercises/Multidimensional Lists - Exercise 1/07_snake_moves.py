rows, cols = list(map(int, input().split()))
snake = input()
idx = 0

for row in range(rows):
    result = ''
    for col in range(cols):
        result += snake[idx % len(snake)]
        idx += 1

    if row % 2 == 0:
        print(result)
    else:
        print(result[::-1])

