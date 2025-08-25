#III. Basic-subclasses-Adam-and-Eve

class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

class God:
    def __init__(self):
        self.humans = [Man(), Woman()]

    def __getitem__(self, index):
        return self.humans[index]

    def __len__(self):
        return len(self.humans)

paradise = God()
print(isinstance(paradise[0], Man))    # True
print(isinstance(paradise[1], Woman))  # True
print(len(paradise))                   # 2
