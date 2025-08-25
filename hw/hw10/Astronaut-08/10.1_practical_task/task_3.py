'''This is DOC string of task 3'''
class Employee:
    '''This is DOC string of Employee'''
    counter = 0
    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary

    def __del__(self):
        Employee.counter -= 1

    def total_employee(self):
        '''This is DOC string of total employee'''
        print(f'Total employee: {Employee.counter}')

    def info(self):
        '''This is DOC string of info'''
        print(f'{self.name} have {self.salary} of salary!')

a = Employee('A', 1500)
b = Employee('B', 1200)
b.total_employee()
a.total_employee()

c = Employee('C', 1050)
a.total_employee()

del b

a.total_employee()
a.info()
c.info()

print()
print(a.__class__.__base__, '\n')
print(a.__class__.__dict__, '\n')
print(a.__class__.__name__, '\n')
print(a.__class__.__module__, '\n')
print(a.__class__.__doc__)
