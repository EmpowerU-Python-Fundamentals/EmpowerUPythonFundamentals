"""Task 3: Employee class"""

class Person:
    """Base person class"""
    def __init__(self, name):
        self.name = name

class Employee(Person):
    """Employee class, based on Person, with sallary info and own methods"""

    __employee_qty = 0

    def __init__(self, name, salary):
        """Each employee has characteristics such as name and salary"""
        super().__init__(name)
        self.salary = salary
        Employee.__employee_qty += 1

    @classmethod
    def get_total_employees(cls):
        """method that prints the total number of employees"""
        return cls.__employee_qty

    def display_employee_info(self):
        """method that displays information about each employee in particular, namely the name and salary"""
        print(f"Name: {self.name}, Salary: ${self.salary:,d}")

# Create employee instances
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 62000)

# Display individual info
emp1.display_employee_info()
emp2.display_employee_info()

print(f"Total employees: {Employee.get_total_employees()}")

# print("Base classes:", Employee.__base__)
# print("Class namespace (__dict__):", Employee.__dict__)
# print("Class name:", Employee.__name__)
# print("Module name:", Employee.__module__)
# print("Documentation (__doc__):", Employee.__doc__)
