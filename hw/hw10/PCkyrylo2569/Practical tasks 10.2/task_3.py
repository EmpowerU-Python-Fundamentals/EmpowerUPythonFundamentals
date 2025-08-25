class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name):
        super().__init__(name)

class Woman(Human):
    def __init__(self, name):
        super().__init__(name)

def God_create():
    return [Man("Adam"), Woman("Eve")]

adam, eve = God_create()
print((adam.name))
print((eve.name))
