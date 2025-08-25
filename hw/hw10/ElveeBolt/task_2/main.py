class Human:
    def __init__(self, name: str):
        self.name = name

    def hello(self):
        return f"Hello, {self.name}!"

    @staticmethod
    def species():
        return "Homosapiens"

    @staticmethod
    def message():
        return "This is message"


if __name__ == '__main__':
    human = Human("ElveeBolt")
    print(human.hello())
    print(human.species())
    print(human.message())