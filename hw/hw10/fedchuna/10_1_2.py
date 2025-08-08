class Human():
    
    species = "Homosapiens"
    
    def __init__(self, name):
        self.name = name
    
    def Greetings(self):
        print(f"Hello {self.name} !!! Nice to see you!!")
        
    def get_name(self):
        return self.name
    
    @classmethod    
    def get_species(cls):
        return cls.species
    
    @staticmethod
    def get_arbitary_message():
        return "This is arbitary message"
        

if __name__ == "__main__":
    person1 = Human("Alex")
    person2 = Human("Igor")
    
    person1.Greetings()
    person1 = person1.get_name()
    person2.Greetings()
    person2 = person2. get_name()    
    
    species = Human.get_species()
    print(f"{person1} : {species}")
    print(f"{person2} : {species}")
    
    arbitary_msg = Human.get_arbitary_message()
    
    print(arbitary_msg)
    