rows, cols = int(input()), int(input())
matrix = []
visited = []

for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)

def dfs(parent, row, col, matrix, visited):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return
    if visited[row][col]:
        return
    if matrix[row][col] != parent:
        return
    
    visited[row][col] = True
    dfs(parent, row - 1, col, matrix, visited)
    dfs(parent, row + 1, col, matrix, visited)
    dfs(parent, row, col - 1, matrix, visited)
    dfs(parent, row, col + 1, matrix, visited)

areas = {}

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        key = matrix[row][col]
        dfs(key, row, col, matrix, visited)

        if key not in areas:
            areas[key] = 1
        else:
            areas[key] += 1

print(f"Areas: {sum(num for num in areas.values())}")
for letter, num in sorted(areas.items(), key=lambda l: l[0]):
    print(f"Letter '{letter}' -> {num}")
