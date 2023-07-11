nums = list(map(int, input().split()))

for i in range(1, len(nums)):
    for j in range(i, 0, -1):
        if nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]

print(*nums, sep=' ')
