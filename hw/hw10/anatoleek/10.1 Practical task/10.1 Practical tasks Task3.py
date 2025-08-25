class Employee:
    """Клас Employee"""
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1  

    @classmethod
    def display_count(cls):
        print(f"Total employees: {cls.employee_count}")

    def display_info(self):
        print(f"Ім’я: {self.name}, Зарплата: {self.salary}")

emp1 = Employee("Андрій", 50000)
emp2 = Employee("Оксана", 60000)

emp1.display_info()
emp2.display_info()

Employee.display_count()

# --- Інформація про клас ---
print("\n--- Інформація про клас Employee ---")
print("Базовий клас (__base__):", Employee.__base__)
print("Простір імен (__dict__):", Employee.__dict__)
print("Назва класу (__name__):", Employee.__name__)
print("Назва модуля (__module__):", Employee.__module__)
print("Документація (__doc__):", Employee.__doc__)
