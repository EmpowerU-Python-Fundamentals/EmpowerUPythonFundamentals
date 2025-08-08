class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    @classmethod
    def print_total(cls):
        return f"Total employees: {cls.total_employees}"

emp1 = Employee("Diana", 5000)
emp2 = Employee("Hryhorii", 6000)

print(emp1.display_info())
print(Employee.print_total())

print("Base classes:", Employee.__bases__)
print("Namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module:", Employee.__module__)
print("Docstring:", Employee.__doc__)