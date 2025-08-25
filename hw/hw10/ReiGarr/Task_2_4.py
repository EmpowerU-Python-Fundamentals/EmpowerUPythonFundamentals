class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.info=f"{name}s age is {age}"
        
    def getInfo(self):
        return f"{self.name}s age is {self.age}"

    def getInfoMethod(self):
        return f"{self.name}s age is {self.age}"