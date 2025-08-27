class Employee:
    """Employee info and counter"""

    EMPLOYEE_COUNTER = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.EMPLOYEE_COUNTER += 1

    def employee_info(self):
        print(f"The employee {self.name} has the salary of {self.salary}")

    @classmethod
    def namber_of_employee(cls):
        print(f"The number of employees is {cls.EMPLOYEE_COUNTER}")


employee1 = Employee("Bill", 1000)
employee2 = Employee("Jack", 2000)
employee3 = Employee("Mark", 3000)

employee1.employee_info()
Employee.namber_of_employee()


print(f"Class is inherited from: {Employee.__base__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation bar: {Employee.__doc__}")
