def start_spring(**example_objects):
    data = {}
    result = ''
    for type, object in example_objects.items():
        if object not in data:
            data[object] = [type]
        else:
            data[object].append(type)

    for key, value in sorted(data.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f'{key}:' + '\n'
        for thing in sorted(value):
            result += f'-{thing}' + '\n'

    return result
