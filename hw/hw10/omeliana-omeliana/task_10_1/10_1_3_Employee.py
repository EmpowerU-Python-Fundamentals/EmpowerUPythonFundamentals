class Employee():

    employee_number = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_number += 1

    def info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def employee_count_print(cls):
        print(f"Number of employees is: {Employee.employee_number}")

e1 = Employee("Anastasiia", 1000000)
e2 = Employee("Mykhailo", 1000000)
e3 = Employee("Uliana", 1000000)
e1.info()
e2.info()
e3.info()
Employee.employee_count_print()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)  
