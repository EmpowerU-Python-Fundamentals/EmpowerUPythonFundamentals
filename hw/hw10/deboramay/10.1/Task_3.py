class Employee:
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_count(self):
        print(f"Total Employees: {Employee.employee_count}")

    def display_employee(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


#Test:
emp1 = Employee("Alice", 5000)
emp1.display_employee()
emp1.display_count()

#Displaying class metadata:
print("\nClass Metadata:")
print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)
