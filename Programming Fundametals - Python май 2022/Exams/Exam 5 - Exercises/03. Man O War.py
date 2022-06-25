pirate_ship_status = list(map(int, input().split('>')))
warship_status = list(map(int, input().split('>')))
max_health = int(input())

while True:
    command = input().split(' ')

    if command[0] == "Retire":
        break

    if command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(warship_status):
            warship_status[index] -= damage
        else:
            continue
        if warship_status[index] <= 0:
            print("You won! The enemy ship has sunken.")
            exit()
    elif command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if 0 <= start_index < len(pirate_ship_status) and 0 <= end_index < len(pirate_ship_status) and damage > 0:
            for j in range(start_index, end_index + 1):
                pirate_ship_status[j] -= damage
                if pirate_ship_status[j] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()
        else:
            continue
    elif command[0] == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(warship_status) and health > 0:
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > max_health:
                pirate_ship_status[index] = max_health
        else:
            continue
    elif command[0] == "Status":
        repair_counter = 0
        low_health = max_health * 0.2
        for section in pirate_ship_status:
            if section < low_health:
                repair_counter += 1
        print(f"{repair_counter} sections need repair.")

print(f"Pirate ship status: {sum(pirate_ship_status)}")
print(f"Warship status: {sum(warship_status)}")
