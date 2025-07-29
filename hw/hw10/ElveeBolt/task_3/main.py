class Employee:
    """
    Employee class documentation
    """
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @classmethod
    def count_employees(cls):
        return cls.count

    def info(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    def __repr__(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary}"


employee1 = Employee("Elvin", 1000)
employee2 = Employee("Oleg", 2000)

print(Employee.count_employees())
print("Base class:", Employee.__base__)
print("Dict:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)
