n = int(input())
word = input()
list = []
filtered_list = []

for i in range(n):
    sentence = input()
    list.append(sentence)

    if word in sentence:
        filtered_list.append(sentence)

print(list)
print(filtered_list)
