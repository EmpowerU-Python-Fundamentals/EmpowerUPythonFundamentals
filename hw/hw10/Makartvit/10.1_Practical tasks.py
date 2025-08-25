class Polygon:
    def __init__(self, sides_count):
        self.sides_count = sides_count


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(sides_count=4)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Human:
    species_name = "Homosapiens"

    def __init__(self, name: str):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

    @classmethod
    def species(cls):
        return f"We are species '{cls.species_name}'."

    @staticmethod
    def random_message():
        return "Today is a great day for Python!"


class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @classmethod
    def total_employees(cls):
        return cls.count

    def info(self):
        return f"Employee: {self.name}, salary: {self.salary}"


print("Task 10.1:")
r = Rectangle(5, 6)
print("  Rectangle sides:", r.sides_count)
print("  Area:", r.area())
print()

print("Task 10.2:")
jon = Human("Jon")
jan = Human("Jan")
print("  Greetings:", jon.greet(), "|", jan.greet())
print("  Species (class method):", Human.species())
print("  Static method:", Human.random_message())
print()

print("Task 10.3:")
e1 = Employee("Al", 3000)
e2 = Employee("Bob", 4500)
print("  Total employees:", Employee.total_employees())
print("  Each info:", e1.info(), "|", e2.info())

print()
print("  __base__:", Employee.__base__)
print("  __bases__:", Employee.__bases__)
print("  __dict__ keys:", list(Employee.__dict__.keys()))
print("  __name__:", Employee.__name__)
print("  __module__:", Employee.__module__)
print("  __doc__:", Employee.__doc__)

