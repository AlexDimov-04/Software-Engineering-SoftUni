students_dict = {}

while True:
    student_info = input()
    if ':' in student_info:
        student_info = student_info.split(':')
        student_name = student_info[0]
        student_id = student_info[1]
        course = student_info[2]
        if course not in students_dict:
            students_dict[course] = {}
        students_dict[course][student_name] = student_id
    else:
        if "_" in student_info:
            student_info = student_info.replace("_", " ")
        break

for key, value in students_dict[student_info].items():
    print(f"{key} - {value}")
