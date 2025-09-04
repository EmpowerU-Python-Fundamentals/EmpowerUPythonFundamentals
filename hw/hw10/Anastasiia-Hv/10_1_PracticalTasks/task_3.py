class Employee:
    """This is the Employee class for storing employee details."""
    
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def display_count(cls):
        print(f"Total number of employees: {cls.employee_count}")

    def display_employee(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

emp1.display_employee()
emp2.display_employee()
Employee.display_count()

print("\n--- Class Information ---")
print("Base classes:", Employee.__base__)
print("Class namespace (__dict__):", Employee.__dict__)
print("Class name (__name__):", Employee.__name__)
print("Module name (__module__):", Employee.__module__)
print("Documentation (__doc__):", Employee.__doc__)