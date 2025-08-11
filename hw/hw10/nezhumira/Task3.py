class Employee:
    
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display_employee(self):
        print(f"Ім’я: {self.name}. Зарплата: {self.salary} грн")

    @staticmethod
    def display_count():
        print(f"Загальна кількість працівників: {Employee.count}")

emp1 = Employee("Оксана", 22000)
emp2 = Employee("Олександр", 28000)

emp1.display_employee()
emp2.display_employee()
Employee.display_count()

print("\nІнформація про клас:")
print("Базовий клас:", Employee.__base__)
print("Простір імен:", Employee.__dict__)
print("Назва класу:", Employee.__name__)
print("Модуль:", Employee.__module__)
print("Документація:", Employee.__doc__)