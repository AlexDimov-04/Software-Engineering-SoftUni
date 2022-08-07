username_data = {}


def new_follower(username):
    if username not in username_data:
        username_data[username] = {'likes': 0, 'comments': 0}
    else:
        return username_data


def like(username, count):
    if username not in username_data:
        username_data[username] = {'likes': count, 'comments': 0}
    else:
        username_data[username]['likes'] += count


def comment(username):
    if username not in username_data:
        username_data[username] = {'likes': 0, 'comments': 1}
    else:
        username_data[username]['comments'] += 1


def blocked(username):
    if username in username_data:
        del username_data[username]
    else:
        print(f"{username} doesn't exist.")


while True:
    command = input()
    if command == "Log out":
        break

    command = command.split(': ')
    user = command[1]

    if command[0] == "New follower":
        new_follower(user)
    elif command[0] == "Like":
        count = int(command[2])
        like(user, count)
    elif command[0] == "Comment":
        comment(user)
    elif command[0] == "Blocked":
        blocked(user)

print(f"{len(username_data)} followers")
for element in username_data:
    print(f"{element}: {username_data[element]['likes'] + username_data[element]['comments']}")
