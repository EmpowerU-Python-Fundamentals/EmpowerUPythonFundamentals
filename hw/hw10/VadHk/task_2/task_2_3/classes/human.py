class Human:
    _humans = []
    
    def __init__(self, name: str):
        self.name = name
        Human._humans.append(self)

    def __str__(self):
        return self.name

    @staticmethod
    def humans():
        return Human._humans
    