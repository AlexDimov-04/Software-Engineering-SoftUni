def vowel_filter(function):
    def wrapper():
        result = function()
        return [w for w in result if w.lower() in 'aeiouy']

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
