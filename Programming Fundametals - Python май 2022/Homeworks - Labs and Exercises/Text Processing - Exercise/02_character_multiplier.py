text1, text2 = input().split()
total_sum = 0

if len(text1) > len(text2):
    for i in range(len(text2)):
        total_sum += ord(text1[i]) * ord(text2[i])
    for i in range(len(text2), len(text1)):
        total_sum += ord(text1[i])
else:
    for i in range(len(text1)):
        total_sum += ord(text1[i]) * ord(text2[i])
    for i in range(len(text1), len(text2)):
        total_sum += ord(text2[i])
print(total_sum)
