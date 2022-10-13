def words_sorting(*args):
    words_dict = {}
    result = ''

    for word in args:
        ascii_sum = 0
        for ch in word:
            ascii_sum += ord(ch)

        words_dict[word] = ascii_sum

    if sum(words_dict.values()) % 2 != 0:
        for word, value in sorted(words_dict.items(), key=lambda x: -x[1]):
            result += f'{word} - {value}' + '\n'

    else:
        for word, value in sorted(words_dict.items()):
            result += f'{word} - {value}' + '\n'

    return result
