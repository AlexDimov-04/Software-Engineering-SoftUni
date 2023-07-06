array = list(map(int, input().split()))

def reverse_arr(idx, arr):
    if idx < 0:
        return arr[idx]
    
    print(arr[idx], end=' ')
    return reverse_arr(idx - 1, arr)

reverse_arr(len(array) - 1, array)
