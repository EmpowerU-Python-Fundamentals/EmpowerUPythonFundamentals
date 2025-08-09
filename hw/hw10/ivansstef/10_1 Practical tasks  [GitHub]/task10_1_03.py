class Employee:
    #Лічилььнік
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def show_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def show_total_employees(cls):
        print(f"Total employees: {cls.count}")

# Створимо кількох емплоєрів:
e1 = Employee("Anna", 4000)
e2 = Employee("Ivan", 5000)

e1.show_info()  
e2.show_info()  
Employee.show_total_employees()  

#вивід  системної  інформації про клас:
print("Base classes:", Employee.__base__)
print("Namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Docstring:", Employee.__doc__)

#просто стрічка :)