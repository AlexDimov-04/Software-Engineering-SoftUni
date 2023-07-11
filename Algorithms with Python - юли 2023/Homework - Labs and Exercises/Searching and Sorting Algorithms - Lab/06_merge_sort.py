nums = list(map(int, input().split()))

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left_half = nums[:mid]
    right_half = nums[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_idx = 0
    right_idx = 0
    
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    
    return merged

print(*merge_sort(nums))
