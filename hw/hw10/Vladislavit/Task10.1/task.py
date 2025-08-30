# ===== ЗАВДАННЯ 1: Класи Polygon і Rectangle =====

class Polygon:
    
    def __init__(self, name):
        self.name = name
    
    def display_info(self):
        print(f"Це {self.name}")


class Rectangle(Polygon):
    
    def __init__(self, width, height):
        super().__init__("прямокутник")
        self.width = width
        self.height = height
    
    def find_square(self):
        return self.width * self.height
    
    def display_info(self):
        super().display_info()
        print(f"Ширина: {self.width}, Висота: {self.height}")
        print(f"Площа: {self.find_square()}")


# ===== ЗАВДАННЯ 2: Клас Human =====

class Human:
    
    def __init__(self, name):
        self.name = name
    
    def welcome_message(self):

        print(f"Привіт, {self.name}! Ласкаво просимо!")
    
    def species_info(self):
        return "Homosapiens"
    
    @staticmethod
    def arbitrary_message():
        return "Людина - це розумна істота, здатна до творчості та самопізнання"


# ===== ЗАВДАННЯ 3: Клас Employee =====

class Employee:
    
    # Класова змінна для підрахунку загальної кількості працівників
    total_employees = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        # Збільшуємо лічильник при створенні нового працівника
        Employee.total_employees += 1
    
    @classmethod
    def print_total_employees(cls):
        print(f"Загальна кількість працівників: {cls.total_employees}")
    
    def display_employee_info(self):
        print(f"Працівник: {self.name}, Зарплата: {self.salary} грн")
    
    def __del__(self):
        Employee.total_employees -= 1


# ===== ДЕМОНСТРАЦІЯ РОБОТИ =====

def main():
    print("=" * 60)
    print("ЗАВДАННЯ 1: Polygon і Rectangle")
    print("=" * 60)
    
    # Створюємо прямокутник
    rect = Rectangle(10, 5)
    rect.display_info()
    print(f"Площа прямокутника: {rect.find_square()}")
    
    print("\n" + "=" * 60)
    print("ЗАВДАННЯ 2: Human")
    print("=" * 60)
    
    # Створюємо людей
    person1 = Human("Олексій")
    person2 = Human("Марія")
    
    person1.welcome_message()
    person2.welcome_message()
    
    print(f"\nВид: {person1.species_info()}")
    print(f"Статичне повідомлення: {Human.arbitrary_message()}")
    
    print("\n" + "=" * 60)
    print("ЗАВДАННЯ 3: Employee")
    print("=" * 60)
    
    # Створюємо працівників
    emp1 = Employee("Іван Петренко", 25000)
    emp2 = Employee("Ольга Сидоренко", 30000)
    emp3 = Employee("Михайло Коваленко", 28000)
    
    # Виводимо інформацію про працівників
    emp1.display_employee_info()
    emp2.display_employee_info()
    emp3.display_employee_info()
    
    # Виводимо загальну кількість
    Employee.print_total_employees()
    
    print("\n" + "=" * 60)
    print("ІНФОРМАЦІЯ ПРО КЛАС EMPLOYEE")
    print("=" * 60)
    
    # Інформація про клас Employee
    print(f"Базові класи: {Employee.__bases__}")
    print(f"Простір імен класу (dict): {list(Employee.__dict__.keys())}")
    print(f"Ім'я класу: {Employee.__name__}")
    print(f"Модуль: {Employee.__module__}")
    print(f"Документація: {Employee.__doc__}")


if __name__ == "__main__":
    main()