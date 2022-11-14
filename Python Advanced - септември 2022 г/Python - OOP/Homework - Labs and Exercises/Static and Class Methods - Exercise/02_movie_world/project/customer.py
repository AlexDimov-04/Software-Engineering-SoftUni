class Customer:
    def __init__(self, name, age, id_num):
        self.name = name
        self.age = age
        self.id = id_num
        self.rented_dvds = []

    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's " \
               f"({', '.join(d.name for d in self.rented_dvds)})"
