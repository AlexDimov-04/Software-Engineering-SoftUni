from collections import deque


def best_list_pureness(*args):
    pureness_elements = {}
    rotations = 0
    numbers = deque([x for x in args[0]])

    for _ in range(args[-1] + 1):
        total_sum = 0
        for idx, num in enumerate(numbers):
            total_sum += idx * num

        if total_sum not in pureness_elements:
            pureness_elements[total_sum] = rotations

        rotations += 1
        numbers.appendleft(numbers.pop())

    return f'Best pureness {max(pureness_elements)} after {pureness_elements[max(pureness_elements)]} rotations'
