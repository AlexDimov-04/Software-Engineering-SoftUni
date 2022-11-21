from collections import deque

eggs = deque(map(int, input().split(', ')))
papers = list(map(int, input().split(', ')))
boxes = 0

while eggs and papers:
    if eggs[0] == 13:
        eggs.popleft()
        papers[0], papers[-1] = papers[-1], papers[0]

    elif eggs[0] <= 0:
        eggs.popleft()

    elif eggs[0] + papers[-1] <= 50:
        boxes += 1
        eggs.popleft()
        papers.pop()

    else:
        eggs.popleft()
        papers.pop()

if boxes:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")
