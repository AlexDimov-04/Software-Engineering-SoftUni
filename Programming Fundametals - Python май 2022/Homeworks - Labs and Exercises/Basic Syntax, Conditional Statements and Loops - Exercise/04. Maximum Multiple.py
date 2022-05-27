divisor = int(input())
boundary = int(input())
largest = 0

for largest_integer in range(1, boundary + 1):
    if largest_integer % divisor == 0 and boundary >= largest_integer > 0:
        largest = largest_integer
print(largest)

