# Create an employee class. Each employee has characteristics such as name and salary. The class should have a
# counter that calculates the total number of employees, as well as a method that prints the total number of
# employees and a method that display information about each employee in particular, namely the name and salary. In
# addition to creating a class, display information about the base classes from which the employees class inherited (
# __base__), the class namespace (__dict__), the class name (__name__), the module name in which the class is defined
# (__module__), the documentation bar (__doc__)

class Employee:
    """
    A class representing an employee of a company.
    Stores information about the name and salary.
    """

    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

        Employee.employee_count += 1

    def display_employee_info(self):
        print(f"Name: {self.name}, Salary: ${self.salary}")

    @classmethod
    def display_total_employees(cls):
        print(f"Total number of employees: {cls.employee_count}")


emp_1 = Employee("Sid", 50000)
emp_2 = Employee("Nancy", 60000)
emp_3 = Employee("John", 55000)

print("--- Information about employees ---")
emp_1.display_employee_info()
emp_2.display_employee_info()
emp_3.display_employee_info()

print("\n--- Total number ---")
Employee.display_total_employees()

print("\n--- Information about class ---")

print("Base classes:", Employee.__base__)
print("\nClass namespace:", Employee.__dict__)
print("\nClass name:", Employee.__name__)
print("\nModule name:", Employee.__module__)
print("\nDocstring", Employee.__doc__)
