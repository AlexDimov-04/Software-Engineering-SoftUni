numbers = list(map(int, input().split(', ')))
index = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]
print(index)