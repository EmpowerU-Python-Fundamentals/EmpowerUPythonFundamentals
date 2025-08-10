class Employee():
    """
    Employee class represents an employee with a name and salary.
    Keeps track of the total number of employees.
    """
    employee_count = 0
    def __init__(self, name: str, salary: float):
        self.name = name.capitalize()
        self.salary = salary
        Employee.employee_count += 1

    def display_info(self): 
        print(f"name: {self.name}, salary: {self.salary}")

    @classmethod
    def display_total_employees(cls):
        print(f"Total employees: {cls.employee_count}")


emp1 = Employee("ivan", 70000)
emp2 = Employee("bohdan", 85000)
emp3 = Employee("mariia", 60000)


emp1.display_info()
emp2.display_info()
emp3.display_info()


Employee.display_total_employees()

print("Base classes (__base__):", Employee.__base__)
print("Class namespace (__dict__):", Employee.__dict__)
print("Class name (__name__):", Employee.__name__)
print("Module name (__module__):", Employee.__module__)
print("Documentation (__doc__):", Employee.__doc__)

