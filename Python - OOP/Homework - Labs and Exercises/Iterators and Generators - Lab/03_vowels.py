class vowels:
    VOWELS_LIST = 'AEIUYOaeiuyo'

    def __init__(self, string):
        self.string = string
        self.vowels_in_text = [el for el in self.string if el in vowels.VOWELS_LIST]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.vowels_in_text:
            raise StopIteration

        return self.vowels_in_text.pop(0)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
