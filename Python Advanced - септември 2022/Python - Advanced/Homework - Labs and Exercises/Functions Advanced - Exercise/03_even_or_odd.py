def even_odd(*nums):
    command = nums[-1]
    nums = nums[:-1]
    if command == 'even':
        result = [x for x in nums if x % 2 == 0]
    elif command == 'odd':
        result = [x for x in nums if x % 2 != 0]

    return result
