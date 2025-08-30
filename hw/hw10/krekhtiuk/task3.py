class Employee:
    count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @classmethod
    def total_employees(cls):
        print(f"Total employees: {cls.count}")
    
    def info(self):
        print(f"Name:{self.name}, Salary:{self.salary}")
    
emp1 = Employee("Vira", 20)
emp2 = Employee("Ihor", 40)
emp3 = Employee("Mak", 100)

emp1.info()
emp2.info()
emp3.info()
Employee.total_employees()
    

print(f"The base classes {Employee.__base__}")
print(f"Namespace {Employee.__dict__}")
print(f"Class name {Employee.__name__}")
print(f"Module name {Employee.__module__}")
print(f"Documentation bar {Employee.__doc__}")