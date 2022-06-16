employers_happiness = list(map(int, input().split(' ')))
factor = int(input())

employers = [current_employer * factor for current_employer in employers_happiness]
happy_employers = list(filter(lambda x: x >= (sum(employers) / len(employers)), employers))

if len(happy_employers) >= len(employers) / 2:
    print(f"Score: {len(happy_employers)}/{len(employers)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employers)}/{len(employers)}. Employees are not happy!")