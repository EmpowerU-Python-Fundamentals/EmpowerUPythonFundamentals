class Person:
    def __init__(self, name,age):
        if isinstance(name, str) and len(name) > 1:
            self.name = name
        else:
            raise TypeError("Name must be string")

        if isinstance(age, int) and age > 0:
            self.age = age
        else:
            raise TypeError("Age must be string")

    @property
    def info(self):
        return f"{self.name}s age is {self.age}"

    def get_info(self):
        return f"{self.name}s age is {self.age}"