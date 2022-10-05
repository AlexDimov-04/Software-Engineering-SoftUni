from string import punctuation

iteration = 0
result = []
with open('text.txt', 'r') as file_read:
    text = file_read.readlines()

for line in text:
    iteration += 1
    current_line = line[:-1]
    letters_count = [x for x in line if x.isalpha()]
    punctuation_marks_count = [x for x in line if x in punctuation]

    result.append(f"Line {iteration}: {current_line} ({len(letters_count)})({len(punctuation_marks_count)})")

with open('output.txt', 'a') as file_write:
    for line in result:
        file_write.write(line + '\n')
