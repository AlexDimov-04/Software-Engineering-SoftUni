from collections import deque

def shortest_path(maze):
    maze_length = len(maze)
    directions = [
        (0, 1), # right
        (0, -1), # left
        (1, 0), # down
        (-1, 0), # up
    ]

    def is_valid_solution(x, y):
        if 0 <= x < maze_length and 0 <= y < maze_length and maze[x][y] != '#':
            return True

    start_x_pos, start_y_pos = None, None
    for i in range(maze_length):
        for j in range(maze_length):
            if maze[i][j] == 'S':
                start_x_pos, start_y_pos = i, j
                break

    visited = set()
    queue = deque([(start_x_pos, start_y_pos, 0)])
    visited.add((start_x_pos, start_y_pos))

    while queue:
        x, y, all_steps = queue.popleft()

        if maze[x][y] == 'E':
            return all_steps

        for current_x, current_y in directions:
            new_x, new_y = x + current_x, y + current_y
            if is_valid_solution(new_x, new_y) and (new_x, new_y) not in visited:
                queue.append((new_x, new_y, all_steps + 1))
                visited.add((new_x, new_y))


n = int(input())
maze = []

for _ in range(n):
    maze.append(input().strip())

print(shortest_path(maze))
