class Employee:
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_info(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")

    @classmethod
    def total_employees(cls):
        print(f"Total number of employees: {cls.employee_count}")


emp1 = Employee("Dimon", 2500)
emp2 = Employee("Kabal", 2600)

emp1.display_info()
emp2.display_info()

Employee.total_employees()

print("Base classes:", Employee.__bases__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Doc string:", Employee.__doc__)
