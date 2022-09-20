from collections import deque

colors = deque(input().split())
MAIN_COLORS = ['red', 'yellow', 'blue']
SECONDARY_COLORS = ['orange', 'purple', 'green']
result_colors = deque()

while colors:
    if len(colors) > 1:
        first, last = colors.popleft(), colors.pop()
        substr = first + last
        substr2 = last + first
        if substr in MAIN_COLORS or substr in SECONDARY_COLORS:
            result_colors.append(substr)
        elif substr2 in MAIN_COLORS or substr2 in SECONDARY_COLORS:
            result_colors.append(substr2)
        else:
            cut_1, cut_2 = first[:-1], last[:-1]

            if cut_1:
                colors.insert(len(colors) // 2, cut_1)
            if cut_2:
                colors.insert(len(colors) // 2, cut_2)

    else:
        substr = colors.popleft()
        if substr in MAIN_COLORS or substr in SECONDARY_COLORS:
            result_colors.append(substr)

for _ in range(len(result_colors)):
    if result_colors[0] == 'orange':
        if 'red' not in result_colors or 'yellow' not in result_colors:
            result_colors.popleft()
        else:
            result_colors.append(result_colors.popleft())
    elif result_colors[0] == 'purple':
        if 'red' not in result_colors or 'blue' not in result_colors:
            result_colors.popleft()
        else:
            result_colors.append(result_colors.popleft())
    elif result_colors[0] == 'green':
        if 'yellow' not in result_colors or 'blue' not in result_colors:
            result_colors.popleft()
        else:
            result_colors.append(result_colors.popleft())
    else:
        result_colors.append(result_colors.popleft())

print(list(result_colors))
