class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

class God(list):
    def __init__(self):
        super().__init__([Man(), Woman()])
