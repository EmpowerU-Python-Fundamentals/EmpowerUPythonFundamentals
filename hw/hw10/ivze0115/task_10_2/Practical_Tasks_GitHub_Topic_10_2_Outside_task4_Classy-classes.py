class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._info = f"{name}s age is {age}"

    @property
    def info(self):
        return self._info

    def getInfo(self):
        return self._info

john = Person("john", 34)
print(john.info)    
print(john.getInfo())
