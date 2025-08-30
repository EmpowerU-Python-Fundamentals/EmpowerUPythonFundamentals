from pprint import pprint

class Employee:
    """Info about an employee"""
    count = 0
    def __init__(self, name, salary):
        self.name = name
        if type(salary) in (int, float):
            self.salary = salary
        Employee.count += 1

    @classmethod
    def display_total_employees(cls):
        print(f"Total number of employees: {Employee.count}")

    def __str__(self):
        return f"Employee {self.name} with salary {self.salary}"

if __name__ == '__main__':
    employee1 = Employee("Alex", 20000)
    employee2 = Employee("Bob", 2500)
    employee1.display_total_employees()
    print(employee1)
    print(employee2)

    print(f"1. Base classes (__bases__):")
    print(f"   {Employee.__bases__}")

    print(f"\n2. Class namespace (__dict__):")
    pprint(Employee.__dict__)

    print(f"\n3. Class name (__name__):")
    print(f"   {Employee.__name__}")

    print(f"\n4. Module name (__module__):")
    print(f"   {Employee.__module__}")

    # __doc__ - строка документации класса
    print(f"\n5. Documentation string (__doc__):")
    print(f"{Employee.__doc__}")