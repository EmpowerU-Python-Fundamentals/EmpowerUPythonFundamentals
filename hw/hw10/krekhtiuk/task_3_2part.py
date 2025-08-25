class Human:
    def __init__(self):
        pass

class Man(Human):
    pass

class Woman(Human):
    pass

def create():
    return [Man(), Woman()]
        