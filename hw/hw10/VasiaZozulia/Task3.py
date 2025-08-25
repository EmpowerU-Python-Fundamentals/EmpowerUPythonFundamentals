class Employee:
    """A class to represent an employee with name and salary."""

    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def total_employees(cls):
        print(f"Total number of employees: {cls.employee_count}")

    def display_employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

def info():
    print("\n--- Class Introspection ---")
    print("Base class:", Employee.__base__)
    print("Class namespace:", Employee.__dict__)
    print("Class name:", Employee.__name__)
    print("Module name:", Employee.__module__)
    print("Docstring:", Employee.__doc__)    
