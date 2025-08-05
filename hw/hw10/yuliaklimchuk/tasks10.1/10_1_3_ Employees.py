class Employees:
    count = 0
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        Employees.count += 1

    def __str__(self):
        return f"Employee: {self.__name}, Salary: {self.__salary}"   
    
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
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        print("setting age")
        if isinstance(salary, float) and salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary. Salary must be a float number greater than zero")

    @classmethod
    def employees_count(cls):
        return f"Number of employees {cls.count}"



em1 = Employees("yulia", 400.0)

em2 = Employees("bob", 500.0)

print(Employees.employees_count())
    
print(em1)
print(em2)

print("Base class:", Employees.__base__)
print("Namespace:", Employees.__dict__)
print("Class name:", Employees.__name__)
print("Module:", Employees.__module__)
print("Docstring:", Employees.__doc__)

