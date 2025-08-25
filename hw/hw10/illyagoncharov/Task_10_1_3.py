class Employee():
    _instances = 0
    instances_list = []

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee._instances += 1
        Employee.instances_list.append(self)

    @classmethod
    def emp_count(cls):
        print(f"Emploees - {cls._instances}:")
        for i in cls.instances_list:
            i.emp_info()
            print("-" * 10)

    @classmethod
    def cls_info(cls):
        print(cls.__bases__)
        print(cls.__dict__)
        print(cls.__name__)
        print(cls.__module__)

    def emp_info(self):
        print(f"{self.name}, salary = {self.salary}")


igor = Employee("Igor", 45)
stepan = Employee("Stepan", 55)
natali = Employee("Natali", 80)

Employee.emp_count()
Employee.cls_info()

igor.emp_info()