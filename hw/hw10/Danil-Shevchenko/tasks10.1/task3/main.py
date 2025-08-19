class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display_employee(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_count(cls):
        print(f"Total Employees: {cls.count}")


emp1 = Employee("Alice", 5000)
emp2 = Employee("Bob", 6000)

emp1.display_employee()
emp2.display_employee()

Employee.display_count()

print("\n--- Class Metadata ---")
print("Base classes:", Employee.__base__)
print("Namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Docstring:", Employee.__doc__)
