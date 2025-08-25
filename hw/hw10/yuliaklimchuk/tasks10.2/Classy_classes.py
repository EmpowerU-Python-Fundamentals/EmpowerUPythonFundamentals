# Your task is to complete this Class, the Person class has been created. 
# You must fill in the Constructor method to accept a name as string and an age as number, 
# complete the get Info property and getInfo method/Info getter which should return johns age is 34


class Person:
    def __init__(self, name,age):
        self.__name = name
        self.__age = age
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and name.isalpha():
            self.__name = name
        else:
            print("Invalid name. Name must be a string containing only letters.") 
            
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if isinstance(age, int) and age>0:
            self.__age = age
        else: 
             print("Invalid age")
                
    
    def info(self):
        return f"{self.__name}s age is {self.__age}"
    


person = Person("Jon", 27)
print (person.info())