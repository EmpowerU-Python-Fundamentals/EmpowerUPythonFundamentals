class Employee:
    e_count = 0
    def __init__(self, salary = None, name =  None):
        self.name = name 
        self.salary = salary
        Employee.e_count += 1
    def show(self):
        print(f"{self.name} грн, {self.salary}")
        print("<<<<<<<<<<<<<<<<<<<<<")
    @classmethod
    def count(cls):
        print(f"Кількість работнічків: {cls.e_count}")
        print("<<<<<<<<<<<<<<<<<<<<<")

e1= Employee("Vasyok", 14500)
e2 = Employee("Valerchik", 15000)
e1.show()
e2.show()
Employee.count()

print("\nClass Information:") 
print("Base classes:", Employee.__base__)
print("Namespace dictionary keys:", list(Employee. __dict__.keys()))
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__ )
        