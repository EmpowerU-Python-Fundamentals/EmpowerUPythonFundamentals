class Employee:
    """This is the Employee class used to store employee details."""
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def total_employees(cls):
        print(f"Total employees: {cls.count}")

# Create employees
emp1 = Employee("John", 5000)
emp2 = Employee("Jane", 7000)

# Display individual info
emp1.display_info()
emp2.display_info()

# Display total employees
Employee.total_employees()

# Meta information
print("\nClass Metadata:")
print("Base class:", Employee.__base__)
print("Namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)