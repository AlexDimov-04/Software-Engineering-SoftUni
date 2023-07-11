numbers = list(map(int, input().split()))
target = int(input())

# iterative method
def binary_search(nums, target):
    left_idx = 0
    right_idx = len(nums) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        mid_el = nums[mid_idx]

        if target == mid_el:
            return mid_idx
        elif target > mid_el:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx  - 1

    return -1

print(binary_search(numbers, target))

# recursive method
"""
def recursive_binary_search(nums, target, left_idx, right_idx):
    mid_idx = (left_idx + right_idx) // 2
    mid_el = nums[mid_idx]

    if left_idx <= right_idx:
        if target == mid_el:
            return mid_idx
        elif target > mid_el:
            return recursive_binary_search(nums, target, mid_idx + 1, right_idx)
        else:
            return recursive_binary_search(nums, target, left_idx, mid_idx - 1)
    else:
        return -1

print(recursive_binary_search(numbers, target, 0, len(numbers) - 1))
"""
