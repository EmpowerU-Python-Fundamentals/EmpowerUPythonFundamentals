class Employee:

    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    def total_number(self):
        print(f"Total number of employees is {Employee.counter}")

    def information(self):
        print(f"The name is {self.name}, the salary is {self.salary}")

print(Employee.__base__,
      Employee.__dict__,
      Employee.__name__,
      Employee.__module__,
      Employee.__doc__)



