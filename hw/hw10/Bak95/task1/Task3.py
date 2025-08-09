class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display_info(self):
        print(f"Ім’я: {self.name}, Зарплата: ${self.salary}")

    @classmethod
    def total_employees(cls):
        print(f"Загальна кількість працівників: {cls.count}")

emp1 = Employee("Ігор", 7000)
emp2 = Employee("Оля", 8000)

emp1.display_info()
emp2.display_info()
Employee.total_employees()

# Інформація про клас
print("Базові класи:", Employee.__base__)
print("Простір імен:", Employee.__dict__)
print("Назва класу:", Employee.__name__)
print("Назва модуля:", Employee.__module__)
print("Документація:", Employee.__doc__)
