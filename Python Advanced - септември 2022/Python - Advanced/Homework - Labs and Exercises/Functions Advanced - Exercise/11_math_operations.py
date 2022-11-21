def math_operations(*args, **kwargs):
    result = ''
    position = 1
    for num in args:
        if position == 1:
            kwargs['a'] += num
        elif position == 2:
            kwargs['s'] -= num
        elif position == 3:
            if num != 0:
                kwargs['d'] /= num
        elif position == 4:
            kwargs['m'] *= num

        position += 1
        if position > 4:
            position = 1

    for ch, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])):
        result += f'{ch}: {value:.1f}' + '\n'

    return result
