stops = input()


def add_stop(idx, text):
    global stops
    if idx in range(len(stops)):
        stops = stops[:idx] + text + stops[idx:]
    else:
        return stops


def remove_stop(start, end):
    global stops
    if start in range(len(stops)) and end in range(len(stops)):
        stops = stops[:start] + stops[end + 1:]
    else:
        return stops


def switch(old, new):
    global stops
    stops = stops.replace(old, new)


while True:
    command = input()
    if command == "Travel":
        break

    command = command.split(':')

    if command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        add_stop(index, string)
    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        remove_stop(start_index, end_index)
    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        switch(old_string, new_string)

    print(stops)

print(f"Ready for world tour! Planned stops: {stops}")
