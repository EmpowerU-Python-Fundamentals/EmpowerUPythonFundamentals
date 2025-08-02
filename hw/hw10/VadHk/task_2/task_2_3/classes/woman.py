from classes.human import Human

class Woman(Human):
    def __init__(self, name):
        super().__init__(name)
        self._gender = "woman"

    