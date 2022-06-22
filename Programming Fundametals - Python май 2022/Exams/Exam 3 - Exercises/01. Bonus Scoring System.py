import math

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
current_student_attendance = 0

for attendance in range(number_of_students):
    student_attendance = int(input())

    total_bonus = (student_attendance / number_of_lectures) * (5 + additional_bonus)

    if total_bonus > max_bonus:
        max_bonus = total_bonus
        current_student_attendance = student_attendance

print(f'Max Bonus: {math.ceil(max_bonus)}.')
print(f'The student has attended {current_student_attendance} lectures.')
