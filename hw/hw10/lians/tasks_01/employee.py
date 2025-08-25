class Employee():
    """Creates loyal workers"""
    count = 0
    
    def __init__(self, name, salary):
        Employee.count += 1
        self.name = name
        self.salary = salary
        
    @staticmethod
    def counter():
        print(f"There are {Employee.count} employees at the current moment.") 
        
    def info(self):
        print(f"Employee {self.name} has salary of ${self.salary}.")
        

dict_str = "\n\t".join(f"{key} : {value}" for key, value in Employee.__dict__.items())

print(f"""\
{Employee.__base__ = }\n
__dict__:\n\t{dict_str}\n
{Employee.__name__ = }
{Employee.__module__ = }
{Employee.__doc__ = }
""")
    
# Test
emp1 = Employee("Servant", 5)
emp1.info()
emp2 = Employee("Slave", 1)
emp2.info()
Employee.counter()
