class Employee():
    cntr = 0
    employees_list = []
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        new_employer = {"name" : self.name, "salary" : self.salary}
        Employee.employees_list.append(new_employer)
        Employee.cntr += 1

    @classmethod
    def get_employee(cls):
        for emp in Employee.employees_list:
            print(f"name: {emp['name']}, salary: {emp['salary']}")        

    @classmethod
    def get_total_number_of_employees(cls):
        return cls.cntr

employee1 = Employee("Alex", 350)
employee2 = Employee("Andrew", 400)

employyers = Employee.get_total_number_of_employees()
print(f"You have {employyers} employers ")

Employee.get_employee()

print(f"Class is inherited from: {Employee.__base__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation bar: {Employee.__doc__}")
