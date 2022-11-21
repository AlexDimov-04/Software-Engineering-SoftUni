class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.count_nums = 0
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count_nums < self.count:
            self.count_nums += 1
            result = self.num
            self.num += self.step
            return result

        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
