class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @classmethod
    def total_employees(cls):
        print(f"Total employees: {cls.count}")

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

emp1 = Employee("John", 5000)
emp2 = Employee("Jane", 6000)
emp1.display_info()
emp2.display_info()
Employee.total_employees()

print("Base classes:", Employee.__base__)
print("Namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)
