class Human():

    def __init__(self, name):
        self.name = name

    def great(self):
        print(f"Hello {self.name}! I am very glad to see you!")

    @classmethod
    def view(cls):
        return f"Glad to report {cls.__name__}, you're Homosapiens!"

    @staticmethod
    def some_static_method():
        return "Hakuna matata!!!"

d = Human("Jack")
d.great()
print(d.view())
print(d.some_static_method())