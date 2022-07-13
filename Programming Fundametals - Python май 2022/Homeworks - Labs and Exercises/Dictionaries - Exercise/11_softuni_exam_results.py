students_results = {}
language_submissions = []

while True:
    command = input()
    if command == "exam finished":
        break

    command = command.split('-')
    if "banned" in command:
        username = command[0]
        students_results.pop(username)
    else:
        username = command[0]
        language = command[1]
        points = int(command[2])
        if username not in students_results.keys():
            students_results[username] = [points]
        else:
            students_results[username].append(points)

        language_submissions.append(language)

print("Results:")
for name, result in students_results.items():
    print(f"{name} | {max(result)}")
print("Submissions:")
language_submissions_unique = set(language_submissions)
for current_language in language_submissions_unique:
    print(f"{current_language} - {language_submissions.count(current_language)}")
