class Employee:
    COUNTER = 0

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        Employee.COUNTER += 1

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @name.setter
    def name(self, value):
        self.__name = value

    @salary.setter
    def salary(self, value):
        self.__salary = value

    @staticmethod
    def get_num_of_employees():
        print(Employee.COUNTER)

    def show_employee_info(self):
        print(f'Name: {self.__name}, Salary: {self.__salary}')

print("(__base__):", Employee.__base__)
print("(__dict__):", Employee.__dict__)
print("(__name__):", Employee.__name__)
print("(__module__):", Employee.__module__)
print("(__doc__):", Employee.__doc__)
