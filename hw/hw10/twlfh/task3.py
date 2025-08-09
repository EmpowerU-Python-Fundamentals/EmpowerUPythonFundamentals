class Employee:
    counter = 0
    def __init__(self, name, salary):
        self.name = name.title()
        self.salary = salary
        Employee.counter += 1

    @classmethod
    def total_employee(cls):
        return f'Total employee: {cls.counter}'

    def info(self):
        return f'Name:{self.name}\nSalary:{self.salary}'

p = Employee('Jack', 1000)
p1 = Employee('Mary', 5599)

print(p.info())
print(Employee.counter)