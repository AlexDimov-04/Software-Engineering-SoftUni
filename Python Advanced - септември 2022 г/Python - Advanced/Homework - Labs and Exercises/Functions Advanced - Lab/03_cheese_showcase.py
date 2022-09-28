def sorting_cheeses(**kwargs):
    sorted_cheese = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    output = ''
    for cheese, value in sorted_cheese:
        sorted_values = sorted(value, key=lambda x: -x)
        output += cheese + '\n'
        output += '\n'.join(str(x) for x in sorted_values) + '\n'
    return output
