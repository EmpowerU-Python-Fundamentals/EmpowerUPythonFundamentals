class Human():
    species = "human"

class Man(Human):
    def __init__(self, name):
        self.name = name

class Woman(Human):
    def __init__(self, name):
        self.name = name

    
def God():
    return [Man("Adam"), Woman("Eve")]
