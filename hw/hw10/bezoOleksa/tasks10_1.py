# task1
class Polygon:
    pass

class Rectangle(Polygon):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'Rectangle({self.a}, {self.b})'

    def area(self):
        return round(self.a * self.b, 4)


# task2
class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f'Hello, {self.name}!'

    @staticmethod
    def species():
        return 'Belongs to the species Homo sapiens'

    @staticmethod
    def smth():
        return 'All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.'


# task3
class Employee(Human):
    """Employee class with name and salary."""
    employees = []

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        Employee.employees.append(self)

    def info(self):
        return f'{self.name} - salary ${self.salary}'

    @classmethod
    def employee_count(cls):
        return len(cls.employees)

    @classmethod
    def employee_info(cls):
        return [ee.info() for ee in cls.employees]

    @classmethod
    def display_class_info(cls):
        return [f'Base class: {cls.__bases__}',
                f'Namespace: {cls.__dict__}',
                f'Class name: {cls.__name__}',
                f'Module name: {cls.__module__}',
                f'Documentation: {cls.__doc__}']

if __name__ == '__main__':
    rect1 = Rectangle(3, 7)
    rect2 = Rectangle(2.3, 4.7)
    for rect in (rect1, rect2):
        print(f'Area of {rect} is {rect.area()}')
    print()
    adam = Human('Adam')
    eve = Human('Eve')
    for pers in (adam, eve):
        print(pers.welcome())
    print(Human.species())
    print(Human.smth())
    print()
    james = Employee('James', 6000)
    victoria = Employee('Victoria', 4400)
    peter = Employee('Peter', 19000)
    print(f'We have {Employee.employee_count()} employees')
    print('\n\t'.join(['Info about them: ', *Employee.employee_info()]))
    print('\n\t'.join(['Info about class: ', *Employee.display_class_info()]))
