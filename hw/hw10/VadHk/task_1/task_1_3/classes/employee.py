class Employee:
    _counter = 0

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        Employee._counter += 1

    def class_info(self):
        print(self.__class__.__name__, self.__class__.__base__, self.__dict__, self.__module__)

    def employee_info(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}"
    
    @staticmethod
    def get_counter():
        print(f"Total Employees: {Employee._counter}")