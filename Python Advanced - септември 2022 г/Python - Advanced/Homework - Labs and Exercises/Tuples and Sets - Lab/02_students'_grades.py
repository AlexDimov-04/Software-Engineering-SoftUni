n = int(input())
students_data = {}

for _ in range(n):
    name, grade = input().split()

    if name not in students_data:
        students_data[name] = [float(grade)]
    else:
        students_data[name].append(float(grade))

for name, grades in students_data.items():
    average = sum(grades) / len(grades)
    nums = [f"{grade:.2f}" for grade in grades]
    print(f"{name} -> {' '.join(nums)} (avg: {average:.2f})")
