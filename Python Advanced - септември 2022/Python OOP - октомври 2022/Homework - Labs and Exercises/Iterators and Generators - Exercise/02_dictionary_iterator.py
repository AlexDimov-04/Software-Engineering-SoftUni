class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.items = list(dictionary.items())

    def __iter__(self):
        return self

    def __next__(self):
        if not self.items:
            raise StopIteration

        return self.items.pop(0)


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
