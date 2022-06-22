inventory = input().split(', ')

while True:
    command = input()

    if command == "Craft!":
        break

    separated = command.split(" - ")

    if separated[0] == "Collect":
        item = separated[1]
        if item not in inventory:
            inventory.append(separated[1])
    elif separated[0] == "Drop":
        item = separated[1]
        if item in inventory:
            inventory.remove(separated[1])
    elif separated[0] == "Combine Items":
        sliced = separated[1].split(':')
        old_item = sliced[0]
        new_item = sliced[1]
        if old_item in inventory:
            new_item_index_place = inventory.index(old_item) + 1
            inventory.insert(new_item_index_place, new_item)
    elif separated[0] == "Renew":
        item = separated[1]
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)

print(', '.join(inventory))
