class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display_employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_total_employees(cls):
        print(f"Total number of employees: {cls.count}")

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

emp1 = Employee("Jane Doe", 3000)
emp2 = Employee("John Doe", 5000)
emp3 = Employee("Kate Doe", 7000)
emp4 = Employee("Max Doe", 9000)

emp1.display_info()
emp2.display_info()
emp3.display_info()
emp4.display_info()
Employee.display_total_employees()

print("\n--- Class Metadata ---")
print("Base classes:", Employee.__bases__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Docstring:", Employee.__doc__)
