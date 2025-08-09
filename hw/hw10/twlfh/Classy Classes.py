class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    @property
    def info(self):
        return f'{self.name}s age is {self.age}'



p = Person(['jhon','jack'], 40)
print(p.info)

