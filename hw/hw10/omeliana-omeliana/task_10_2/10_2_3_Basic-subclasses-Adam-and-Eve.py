class Human():
    """
    Basic-subclasses-Adam-and-Eve
    """
    def __init__(self):
        pass
    
class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(), Woman()]