from collections import defaultdict

contest_and_pass = defaultdict(str)
competition_data = {}
valid = False

while True:
    command = input()
    if command == "end of contests":
        break
    command = command.split(':')
    contest, password = command
    contest_and_pass[contest] = password

while True:
    command = input()
    if command == "end of submissions":
        break

    command = command.split('=>')
    contest, password, username, points = command
    if contest in contest_and_pass.keys() and password in contest_and_pass.values():
        valid = True

    if valid:
        if username not in competition_data:
            competition_data[username] = {}
            competition_data[username][contest] = int(points)
        if contest not in competition_data[username]:
            competition_data[username][contest] = int(points)
        if int(points) > competition_data[username][contest]:
            max_points = int(points)
            competition_data[username][contest] = max_points
    valid = False

highest_score_person = ""
highest_score = 0
for key, value in competition_data.items():
    for name in competition_data.keys():
        score_for_user = sum(value.values())
        if score_for_user > highest_score:
            highest_score = score_for_user
            highest_score_person = name
        break
print(f"Best candidate is {highest_score_person} with total {highest_score} points.")
print("Ranking:")

for name in sorted(competition_data.keys()):
    print(name)
    for contest, points in sorted(competition_data[name].items(), key=lambda item: -item[1]):
        print(f"#  {contest} -> {points}")
