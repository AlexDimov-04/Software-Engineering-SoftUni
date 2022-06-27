numbers_list = input().split(' ')
init_message = input()
message_list = []

for sequence in numbers_list:
    current_sum = 0
    for i in sequence:
        current_sum += int(i)

    current_sum %= len(init_message)

    message_list.append(init_message[current_sum])
    init_message = init_message.replace(init_message[current_sum], '', 1)

print(''.join(message_list))
