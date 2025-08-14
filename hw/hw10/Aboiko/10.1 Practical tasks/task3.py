class Employee:
    """
    A class to show an employee with a name and salary.
    Also can be viewed the total number of employees.
    """

    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def print_total_employees(cls):
        print(f"Total number of employees: {cls.employee_count}")

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


emp1 = Employee("Anton", 2500)
emp2 = Employee("Andrii", 2700)

emp1.display_info()
emp2.display_info()

Employee.print_total_employees()


print("\nClass Info:\n")
print("Base classes:", Employee.__base__, "\n")
print("Class namespace:", Employee.__dict__, "\n")
print("Class name:", Employee.__name__, "\n")
print("Module name:", Employee.__module__, "\n")
print("Documentation:", Employee.__doc__)