class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name="Adam"):
        super().__init__(name)

class Woman(Human):
    def __init__(self, name="Eve"):
        super().__init__(name)

def God():
    return [Man(), Woman()]