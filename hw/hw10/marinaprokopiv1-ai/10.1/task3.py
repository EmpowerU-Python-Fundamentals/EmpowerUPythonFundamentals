class Employee:
    count = 0  # счётчик сотрудников

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @classmethod
    def total_employees(cls):
        return cls.count

    def employee_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"