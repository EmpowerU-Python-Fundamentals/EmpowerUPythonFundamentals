class Polygon:
    def __init__(self, width, height):
        self.width=width
        self.height=height

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(width, height)

    def calculate(self):
        print(self.width*self.height)

t = Rectangle(2, 3)
t.calculate()

class Human:
    def __init__(self,name):
        self.name=name

    def welcome(self):
        print(f"Hello, {self.name}.")

    @classmethod
    def species(cls):
        return "Вид: Homosapiens"

    @staticmethod
    def message():
        return "Привіт"

h1 = Human("Анна")
h1.welcome()
print(Human.species())
print(Human.message())

class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def show_info(self):
        print(f"Ім'я: {self.name}, Зарплата: {self.salary}")

    @classmethod
    def total_employees(cls):
        print(f"Всього співробітників: {cls.count}")

    @staticmethod
    def class_info():
        print(f"Базовий клас: {Employee.__base__}")
        print(f"Словник атрибутів: {Employee.__dict__}")
        print(f"Ім'я класу: {Employee.__name__}")
        print(f"Модуль: {Employee.__module__}")
        print(f"Документація: {Employee.__doc__}")

e1 = Employee("Оля", 1000)
e2 = Employee("Петро", 1200)

e1.show_info()
e2.show_info()

Employee.total_employees()

Employee.class_info()