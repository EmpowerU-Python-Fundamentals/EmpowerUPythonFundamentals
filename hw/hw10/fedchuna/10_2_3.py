class Human():
    
    def __init__(self):
        pass

class Man(Human):

    def __init__(self):
        super().__init__()
        self.name = "Adam"

class Woman(Human):

    def __init__(self):
        super().__init__()
        self.name = "Eve"

def God():

    adam = Man()
    eve = Woman()
    return [adam, eve]

paradise = God()
