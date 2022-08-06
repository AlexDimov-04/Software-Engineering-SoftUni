import re

sentence = input()
specific_word = input()

pattern = fr"\b{specific_word}\b"
result = re.findall(pattern, sentence, re.IGNORECASE)

print(len(result))
