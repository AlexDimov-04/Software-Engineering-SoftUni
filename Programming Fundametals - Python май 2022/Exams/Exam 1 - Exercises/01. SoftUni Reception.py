first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students = int(input())
hours_count = 0

served_students_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency

while students > 0:
    students -= served_students_per_hour
    hours_count += 1

    if hours_count % 4 == 0:
        hours_count += 1

print(f'Time needed: {hours_count}h.')
