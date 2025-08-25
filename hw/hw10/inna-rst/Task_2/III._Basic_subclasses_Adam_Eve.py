class Human:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

class Man(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.gender = "man"



class Woman(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.gender = "woman"


def God():
    return [Man("Adam", 25), Woman("Eve", 25)]