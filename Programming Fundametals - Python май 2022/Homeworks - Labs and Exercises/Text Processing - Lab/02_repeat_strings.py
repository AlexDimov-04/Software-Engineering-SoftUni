strings = input().split(' ')

result = [word * len(word) for word in strings]
print(''.join(result))

# final_str = ""
# for text in strings:
#     final_str += text * len(text)
# print(final_str)
