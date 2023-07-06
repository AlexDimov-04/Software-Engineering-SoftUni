n = int(input())
array = [None] * n

def loop_iteration(idx, arr):
    if idx >= len(arr):
        print(*arr, sep=' ')
        return
    
    for i in range(1, n + 1):
        arr[idx] = i
        loop_iteration(idx + 1, arr)

loop_iteration(0, array)
