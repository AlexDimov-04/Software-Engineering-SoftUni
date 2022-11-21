def flights(*args):
    flight_data = {}
    for n in range(0, len(args), 2):
        if args[n] == 'Finish':
            break

        elif args[n] not in flight_data:
            flight_data[args[n]] = args[n + 1]

        else:
            flight_data[args[n]] += args[n + 1]

    return flight_data
