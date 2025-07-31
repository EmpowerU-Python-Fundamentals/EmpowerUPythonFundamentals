# class Encapsulation:
#     def __init__(self, a, b, c):
#         self.public = a
#         self._protected = b
#         self.__private = c
#     def __str__(self):
#         return f"Encapsulation(public={self.public}, _protected={self._protected}, __private={self.__private})" 


# e = Encapsulation(1, 2, 3)
# print(e)  # Output: Encapsulation(public=1, _protected=2, __private=3)
# print(e.public)        # Output: 1
# print(e._protected)     # Output: 2
# # print(e.__private)  # Raises AttributeError: 'Encapsulation' object has no attribute '__private'
# print(e._Encapsulation__private)  # Accessing private attribute using name mangling: Output: 3
# e._Encapsulation__private = 4
# print(e)  # Output: Encapsulation(public=1, _protected=2, __private=4)

class User:
    # def __init__(self, name, age):
    #     self.__name = name
    #     self.__age = age

    def __str__(self):
        return f"User: {self.__name}, Age: {self.__age}"   

    def get_name(self):
        print("getting name")
        return self.__name
    def set_name(self, name):
        print("setting name")
        if isinstance(name, str) and name.isalpha():
            self.__name = name
        else:
            print("Invalid name. Name must be a string containing only letters.")
    name = property(get_name, set_name)
    
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        print("setting age")
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            print("Invalid age. Age must be a positive integer.")

    def f():
        """A simple method to demonstrate encapsulation."""
        print("This is a method inside the User class.")
    
    @classmethod
    def g(cls):
        print("This is a class method inside the User class."   )
        print(cls)

user = User("Alice", 30)
# user = User()
# user.__dict__['_User__name'] = "Alice"  # Simulating private attribute
# user.__dict__['_User__age'] = 30  # Simulating private attribute
print(user)
# print(user.get_name())  # Output: Alice
# user.set_name("Bob")
# print(user)  # Output: User: Bob, Age: 30
# user.set_name("Alice123")  # Invalid name
# # Output: Invalid name. Name must be a string containing only letters.
# print(user)
print(user.name)  # Output: Bob
user.name = "Charlie"  # Using property setter
print(user)  # Output: User: Charlie, Age: 30
print(user.age)  # Output: 30
user.age = 35  # Using property setter
print(user)  # Output: User: Charlie, Age: 35
user.age = -5  # Invalid age
print(user)  # Output: User: Charlie, Age: 35

# user.f()  # Output: This is a method inside the User class.
user.g()  # Output: This is a class method inside the User class.


from abc import ABC, abstractmethod


class TC:
    pass

