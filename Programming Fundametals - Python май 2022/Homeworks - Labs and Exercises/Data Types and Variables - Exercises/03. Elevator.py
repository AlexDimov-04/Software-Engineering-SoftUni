from math import ceil

num_people = int(input())
elevator_capacity = int(input())
courses = 0

courses = ceil(num_people / elevator_capacity)
print(courses)
