class Employee:
    """A class to represent an employee."""

    _init_number_of_employees = 0

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        Employee._init_number_of_employees += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary

    @classmethod
    def get_number_of_employees(cls):
        print(f"Total employees: {cls._init_number_of_employees}")

    def employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


# example usage
all_employees = [
    Employee("Alice", 50000),
    Employee("Bob", 60000),
    Employee("Charlie", 70000),
]

for single_employee in all_employees:
    single_employee.employee_info()

Employee.get_number_of_employees()


print("(__base__):", Employee.__base__)
print("(__dict__):", Employee.__dict__)
print("(__name__):", Employee.__name__)
print("(__module__):", Employee.__module__)
print("(__doc__):", Employee.__doc__)
