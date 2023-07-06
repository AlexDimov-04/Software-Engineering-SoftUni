rows = int(input())
cols = int(input())

land = [['-'] * cols for _ in range(rows)]
paths = 0

def find_all_paths(row, col, land):
    global paths
    
    if row < 0 or col < 0 or row >= len(land) or col >= len(land[0]):
        return
    
    if row == (rows - 1) and col == (cols - 1):
        paths += 1
    else:
        land[row][col] = 'v'

        find_all_paths(row + 1, col, land) # down
        find_all_paths(row, col + 1, land) # right

        land[row][col] = '-'

find_all_paths(0, 0, land)
print(paths)