groceries = input().split('!')

while True:
    command = input()

    if command == "Go Shopping!":
        break

    separation = command.split(' ')

    if separation[0] == 'Urgent':
        item = separation[1]
        if item not in groceries:
            groceries.insert(0, item)
    elif separation[0] == 'Unnecessary':
        item = separation[1]
        if item in groceries:
            groceries.remove(item)
    elif separation[0] == 'Correct':
        old_item = separation[1]
        new_item = separation[2]
        if old_item in groceries:
            index_old_item = groceries.index(old_item)
            groceries.remove(old_item)
            groceries.insert(index_old_item, new_item)
    elif separation[0] == 'Rearrange':
        item = separation[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

print(', '.join(groceries))
