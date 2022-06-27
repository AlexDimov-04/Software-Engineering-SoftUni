nums = list(map(int, input().split(' ')))
time_left_car = 0.0
time_right_car = 0.0
middle_index = len(nums) // 2
first_car = nums[0:middle_index]
second_car = nums[-1:middle_index:-1]

for time_1 in first_car:
    time_left_car += time_1
    if time_1 == 0:
        time_left_car *= 0.8

for time_2 in second_car:
    time_right_car += time_2
    if time_2 == 0:
        time_right_car *= 0.8

if time_left_car < time_right_car:
    print(f"The winner is left with total time: {time_left_car:.1f}")
elif time_left_car > time_right_car:
    print(f"The winner is right with total time: {time_right_car:.1f}")
