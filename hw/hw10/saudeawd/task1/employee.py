"""eployee"""
class Employee:
    """eployee"""
    counter = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1
    @classmethod
    def total_employees(cls):
        """total number of eployees
        Returns:
            str: message
        """
        return f'Total number of employee is {cls.counter}'
    def display_info(self):
        """displayes information
        Returns:
            str: message
        """
        return f'Employee`s name is {self.name} and salary is {self.salary}'

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(emp1.display_info())
print(emp2.display_info())
print(Employee.total_employees())

print("Base classes:", Employee.__base__)
print("Namespace:", Employee.__dict__.keys())
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)
