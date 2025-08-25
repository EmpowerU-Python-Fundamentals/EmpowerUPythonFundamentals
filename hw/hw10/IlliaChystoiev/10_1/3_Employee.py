class Employee:
    count = 0

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = float(salary)
        Employee.count += 1

    def display_employee(self) -> None:
        print(f"Name: {self.name}, Salary: {self.salary:.2f}")

    @classmethod
    def print_total(cls) -> None:
        print(f"Total Employees: {cls.count}")


if __name__ == "__main__":
    e1 = Employee("Anna", 25000)
    e2 = Employee("Bohdan", 32000)
    e3 = Employee("Solomiia", 28000)

    e1.display_employee()
    e2.display_employee()
    e3.display_employee()
    Employee.print_total()


    print("\nClass Introspection:")

    cls = Employee  # зручно мати коротке ім'я
    print("base (first base):", cls.__base__)
    print("bases (all):", cls.__bases__)
    print("__dict__ keys:", list(cls.__dict__.keys()))
    print("__name__:", cls.__name__)
    print("__module__:", cls.__module__)
    print("__doc__:", cls.__doc__)
