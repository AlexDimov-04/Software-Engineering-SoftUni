courses_data = {}

while True:
    course_and_student_name = input()
    if course_and_student_name == "end":
        break

    course_and_student_name = course_and_student_name.split(' : ')
    course = course_and_student_name[0]
    name = course_and_student_name[1]

    if course not in courses_data.keys():
        courses_data[course] = []
    courses_data[course].append(name)

for course_name, registered_students in courses_data.items():
    print(f"{course_name}: {len(registered_students)}")
    print('\n'.join(f"-- {x}" for x in registered_students))
