class Human:
    def __init__(self, name):
        self.name = name.title()

    def welcome_message(self):
        return f'Hello {self.name}!'

    @classmethod
    def info(cls):
        return f'Humans are species of Homo sapiens.'

    @staticmethod
    def message():
        return f'Enjoy your trip!'


name = Human('Jack')
print(name.welcome_message())
print(name.info())
print(name.message())


