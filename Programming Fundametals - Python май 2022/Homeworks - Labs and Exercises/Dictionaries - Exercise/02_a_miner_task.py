resources = {}

while True:
    command = input()
    if command == "stop":
        break

    number = int(input())
    if command not in resources:
        resources[command] = number
    else:
        resources[command] += number

for key, value in resources.items():
    print(f"{key} -> {value}")
