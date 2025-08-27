class Employee:
    """This is the Employee class"""
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @classmethod
    def total_employees(cls):
        return cls.count

    def info(self):
        return f"Name: {self.name}, Salary: {self.salary}"


e1 = Employee("John", 5000)
e2 = Employee("Anna", 6000)

print(e1.info())
print(e2.info())
print("Total employees:", Employee.total_employees())

print("Base class:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module:", Employee.__module__)
print("Docstring:", Employee.__doc__)
