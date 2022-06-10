sums_list_as_strings = input().split(', ')
beggars = int(input())
final_list = []
index_counter = 0
sums_lists_as_digits = []

for element in sums_list_as_strings:
    sums_lists_as_digits.append(int(element))
while index_counter < beggars:
    sum_of_current_beggar = 0
    for current_index in range(index_counter, len(sums_lists_as_digits), beggars):
        sum_of_current_beggar += sums_lists_as_digits[current_index]
    index_counter += 1
    final_list.append(sum_of_current_beggar)
print(final_list)