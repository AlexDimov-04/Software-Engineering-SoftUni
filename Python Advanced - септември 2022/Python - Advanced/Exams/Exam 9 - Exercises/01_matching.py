from collections import deque

males = list(map(int, input().split()))
females = deque(map(int, input().split()))
matches = 0

while males and females:

    if males[-1] <= 0 or females[0] <= 0:
        if males[-1] <= 0:
            males.pop()

        if females[0] <= 0:
            females.popleft()

    elif males[-1] % 25 == 0 or females[0] % 25 == 0:
        if males[-1] % 25 == 0:
            males.pop()
            males.pop()

        if females[0] % 25 == 0:
            females.popleft()
            females.popleft()

    elif males[-1] == females[0]:
        females.popleft()
        males.pop()
        matches += 1

    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join(map(str, males[::-1]))}")
else:
    print(f"Males left: none")

if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print("Females left: none")

