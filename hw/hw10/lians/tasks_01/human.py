class Human():
    def __init__(self, name):
        self.name = name
    
    @property   
    def species(self):
        return "Homo sapiens"
        
    def greeting(self):
        return f"Welcome to this world, {self.name}!"
        
    @staticmethod
    def message():
        return "Dear aliens, Earth is already populated. Find some other place."
          
                
# Test
person = Human("Lians")
print(f"{person.name = }, {person.species = }")
print(f"Greeting: {person.greeting()}\nMessage: {person.message()}")
