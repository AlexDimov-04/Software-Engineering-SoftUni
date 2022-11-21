from functools import reduce


def fill_the_box(*args):
    total_capacity = 0
    size = reduce(lambda x, y: x * y, args[:3])
    cubes = args[3:]

    for n in cubes:
        if n == "Finish":
            break

        total_capacity += n

        if total_capacity == size:
            break

    if total_capacity < size:
        return f"There is free space in the box. You could put {size - total_capacity} more cubes."
    else:
        return f"No more free space! You have {total_capacity - size} more cubes."
