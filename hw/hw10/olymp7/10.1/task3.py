class Employee:
    _employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee._employee_count += 1

    def total_employees(self):
        return f"Total number of employees: {Employee._employee_count}"

    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    @classmethod
    def get_base_info(cls):
        return f"Base classes: {cls.__bases__},\nNamespace: {cls.__dict__},\nClass name: {cls.__name__},\n" \
               f"Module: {cls.__module__},\nDocumentation: {cls.__doc__}"


emp1 = Employee("John Doe", 5000)
emp2 = Employee("Jane Smith", 6000)
print(emp1.total_employees())
print(emp1.display_info())
print(emp2.display_info())
print(Employee.get_base_info())