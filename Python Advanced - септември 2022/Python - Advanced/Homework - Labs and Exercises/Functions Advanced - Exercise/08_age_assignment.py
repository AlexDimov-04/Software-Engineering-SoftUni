def age_assignment(*args, **kwargs):
    result = ''
    people = {}
    for char, years in sorted(kwargs.items()):
        for name in sorted(args):
            if name.startswith(char):
                people[name] = years
                result += f'{name} is {years} years old.' + '\n'

    return result
