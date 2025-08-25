# Task 3: Employee

class Employee:
    employee_count = 0 

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def total_employees(cls):
        return f"Total employees: {cls.employee_count}"

    def display_info(self):
        return f"Employee: {self.name}, Salary: {self.salary}"


# Example usage
emp1 = Employee("Dmytro", 5000)
emp2 = Employee("Olena", 7000)

print("Task3 ->", emp1.display_info())
print("Task3 ->", emp2.display_info())
print("Task3 ->", Employee.total_employees())

# Additional class information
print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module:", Employee.__module__)
print("Docstring:", Employee.__doc__)
