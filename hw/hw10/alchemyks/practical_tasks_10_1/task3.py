class Employee:
    counter = 0
   
    def __init__(self, name, position, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    @classmethod
    def get_employee_count(cls):
        return cls.counter

    def get_employee_info(self):
        return f"Name: {self.name}, Salary: ${self.salary}"
    
if __name__ == "__main__":
    emp1 = Employee("Alice", "Developer", 70000)
    emp2 = Employee("Bob", "Designer", 65000)
    emp3 = Employee("Charlie", "Manager", 80000)

    print(emp1.get_employee_info())
    print(emp2.get_employee_info())
    print(emp3.get_employee_info())
    print(f"Total Employees: {Employee.get_employee_count()}")

    print(Employee.__base__)
    print(Employee.__dict__)
    print(Employee.__name__)
    print(Employee.__module__)
    print(Employee.__doc__)