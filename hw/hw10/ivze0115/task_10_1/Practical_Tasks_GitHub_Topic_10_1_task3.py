class Employee:
    """
    Class representing an employee with a name and salary.
    Counter calculates the total number of employees.
    """

    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def show_total_amployees_count(cls):
        print(f"Total Employees: {cls.employee_count}")


if __name__ == '__main__':
    emp_1 = Employee("Mykola", 40000)
    emp_2 = Employee("Roman", 30000)
    emp_3 = Employee("Vasyl", 35000)
    emp_1.display_info()
    emp_2.display_info()
    emp_3.display_info()
    Employee.show_total_amployees_count()
    print("\nClass Metadata:")
    print("Base class:", Employee.__base__)
    print("Class namespace (keys):", list(Employee.__dict__.keys()))
    print("Class name:", Employee.__name__)
    print("Module name:", Employee.__module__)
    print("Documentation bar:", Employee.__doc__)
