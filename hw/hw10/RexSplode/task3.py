class Employee:
    counter = 0
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        Employee.counter += 1
    
    def __str__(self):
        return f"Employee ({self.name=},{self.salary=}"
    
    @classmethod
    def print_employee_count(cls) -> None:
        print(f"Total number of employees: {cls.counter}")
    

steve = Employee("Steve", 100.5)
larry = Employee("Larry", 97.8)
print(steve)
print(larry)

Employee.print_employee_count()
print(Employee.__base__)
print(Employee.__name__)
print(Employee.__doc__)
print(Employee.__module__)