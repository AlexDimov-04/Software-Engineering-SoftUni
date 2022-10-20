def list_manipulator(*args):
    numbers = [x for x in args[0]]
    command = args[1]
    position = args[2]
    other_parameters = list(args[3:])

    if command == 'add' and position == 'beginning':
        numbers = other_parameters + numbers

    elif command == 'add' and position == 'end':
        numbers += other_parameters

    elif command == 'remove' and position == 'beginning':
        if other_parameters:
            n = ''.join(map(str, other_parameters))
            numbers = numbers[int(n):]
        else:
            numbers = numbers[1:]

    elif command == 'remove' and position == 'end':
        if other_parameters:
            n = ''.join(map(str, other_parameters))
            numbers = numbers[:len(numbers) - int(n)]
        else:
            numbers = numbers[:-1]

    return numbers
