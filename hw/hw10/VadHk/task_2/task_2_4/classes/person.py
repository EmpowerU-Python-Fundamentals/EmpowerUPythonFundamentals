class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self._info = f"{self.name} is {self.age} years old"

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
    
    @property
    def info(self):
        return self._info