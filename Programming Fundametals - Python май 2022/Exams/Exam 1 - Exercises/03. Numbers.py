def average(integer):
    return sum(integer_list) / len(integer_list)


iteration = 0
nums_greater_than_average = []
integer_list = [int(x) for x in input().split(' ')]
average_number = average(integer_list)

if len(integer_list) > 1:
    for current_num in integer_list:
        if current_num > average_number:
            nums_greater_than_average.append(current_num)

    nums_greater_than_average.sort(reverse=True)

    for integer_values in nums_greater_than_average:
        iteration += 1
        print(integer_values, end=' ')
        if iteration == 5:
            break
else:
    print('No')


