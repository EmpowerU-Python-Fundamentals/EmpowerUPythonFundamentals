"""My way of solving task 3"""


class Employee:
    """
    Class Employee represents an employee with a name and salary.
    Counts the total number of employees created.
    """
    count = 0  # Counter that calculates the total number of employees

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display_info(self):
        """Return employee's info (name & salary)"""
        print(f"Ім'я: {self.name}, Зарплата: {self.salary}")

    @classmethod
    def total_employees(cls):
        """Return the total number of employees created"""
        print(f"Загальна кількість працівників: {cls.count}")
