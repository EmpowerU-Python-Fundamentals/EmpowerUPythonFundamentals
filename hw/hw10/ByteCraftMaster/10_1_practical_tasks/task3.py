class Employee():
    """An employee class"""
    number_of_employees=0
    def __init__(self, name, salary):
        self.name = name
        self.salary= salary
        Employee.number_of_employees+=1

    @classmethod
    def get_number_of_employees(cls):
        print (f"Total number of employees = {cls.number_of_employees}") 
    
    def get_employee_info(self):
        print(f"Employee name {self.name}, salary {self.salary}")
    

print (f"Base classes from which the employee class is inherited {Employee.__base__}")
print (f"The class namespace {Employee.__dict__}")
print (f"The class name {Employee.__name__}")
print (f"The module name in which the class is defined {Employee.__module__}")
print (f"The documentation bar {Employee.__doc__}")