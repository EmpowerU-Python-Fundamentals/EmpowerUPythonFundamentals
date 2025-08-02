class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.info = f"{name}s age is {age}"
    @property
    def getInfo(self):
        return self.info
