class Human():
    species = "Homosapiens" 

    def __init__(self, name):
        self.name = name
    
    def hello(self):
        print (f"Hi, {self.name}")

    @classmethod
    def spec_return(cls):
        return f"Species are {cls.species}"
    
    @staticmethod
    def arbitrary_message():
        return "Welcome"

person = Human("Nastia")
person.hello()
print(Human.spec_return())
print(Human.arbitrary_message())