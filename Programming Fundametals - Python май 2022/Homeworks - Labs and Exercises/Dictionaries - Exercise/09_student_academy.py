n = int(input())
students_data = {}
count = 1
average = 0

for _ in range(n):
    student_name = input()
    grade = float(input())

    if grade >= 4.50 or student_name in students_data.keys():
        if student_name not in students_data.keys():
            students_data[student_name] = grade
        elif student_name in students_data.keys():
            count += 1
            students_data[student_name] += grade
            average = students_data[student_name] / count
            students_data[student_name] = average
            count = 1

for name, average_grade in students_data.items():
    print(f"{name} -> {average_grade:.2f}")
