first_sequence = {int(x) for x in input().split()}
second_sequence = {int(x) for x in input().split()}
n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == "Add":
        nums = [int(x) for x in command if x.isdigit()]
        if command[1] == "First":
            first_sequence.update(nums)
        elif command[1] == "Second":
            second_sequence.update(nums)

    elif command[0] == "Remove":
        nums = [int(x) for x in command if x.isdigit()]
        if command[1] == "First":
            for num in nums:
                first_sequence.discard(num)
        elif command[1] == "Second":
            for num in nums:
                second_sequence.discard(num)

    elif command[0] == "Check":
        print(second_sequence.issubset(first_sequence))

sorted_first_seq = sorted(first_sequence)
sorted_second_seq = sorted(second_sequence)

print(*sorted_first_seq, sep=', ')
print(*sorted_second_seq, sep=', ')
