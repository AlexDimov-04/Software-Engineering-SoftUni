text = input()
strength = 0
final_text = ""

for index in range(len(text)):
    if strength > 0 and text[index] != ">":
        strength -= 1
    elif text[index] == ">":
        strength += int(text[index + 1])
        final_text += text[index]
    else:
        final_text += text[index]

print(final_text)
