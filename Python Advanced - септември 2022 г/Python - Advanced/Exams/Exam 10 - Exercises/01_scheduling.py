jobs = list(map(int, input().split(', ')))
index = int(input())
total_clock_cycles = 0

for num in sorted(jobs):
    if num <= jobs[index]:
        total_clock_cycles += num

print(total_clock_cycles)
