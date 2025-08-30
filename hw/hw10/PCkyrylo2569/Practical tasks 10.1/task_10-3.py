class Employee:
    employee_count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def total_employees(cls):
        print(f"Total number of employees: {cls.employee_count}")

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

emp1 = Employee("Alice", 5000)
emp2 = Employee("Bob", 6000)

emp1.display_info()
emp2.display_info()
Employee.total_employees()

print("\nClass Metadata:")
print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Docstring:", Employee.__doc__)