class Employee:
    """This class represents an employee with a name and salary."""

    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_total_employees(cls):
        print(f"Total number of employees: {cls.employee_count}")

employees = []

while True:
    name = input("Enter employee name (or press Enter with empty string to finish): ").strip()
    if name == "":
        break
    salary = float(input(f"Enter salary for {name}: "))

    employee = Employee(name, salary)
    employees.append(employee)

print("\n--- Employee Information ---")
for emp in employees:
    emp.display_employee_info()

Employee.display_total_employees()

print("\n--- Class Metadata ---")
print("Base classes:", Employee.__bases__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Docstring:", Employee.__doc__)
