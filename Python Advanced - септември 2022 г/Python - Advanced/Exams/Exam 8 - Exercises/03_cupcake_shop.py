def stock_availability(*args):
    cupcakes = [x for x in args[0]]
    command = args[1]

    if command == 'delivery':
        boxes = args[2:]
        cupcakes.extend(boxes)

    elif command == 'sell':
        data = args[2:]
        if data:
            if isinstance(args[-1], int):
                del cupcakes[:args[-1]]
            else:
                for flavor in data:
                    while flavor in cupcakes:
                        cupcakes.remove(flavor)
        else:
            cupcakes.pop(0)

    return cupcakes
