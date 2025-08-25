# Task3.
# Create an employee class.
#   Each employee has characteristics such as name and salary.
# The class should have 
#   a counter that calculates the total number of employees,
#   as well as a method that prints the total number of employees
#   and a method that displays information 
#       about each employee in particular, namely the name and salary.
# In addition to creating a class,
#   display information about the base classes
#       from which the employee class is inherited (__base__),
#   the class namespace (__dict__)
#   the class name (_name_),
#   the module name in which the class is defined (__mmodule__)
#   the documentation bar (_doc_)

class foo():
    pass

class bar(foo):
    pass

class employee(bar):
    """Describes an employee by it's name and salary."""

    # A class variable that counts of active employees instances
    _employees_count = 0

    def __init__(self, name: str, salary: float):
        """Initializes an employee instance."""
        self._name = name
        self._salary = salary
        __class__._employees_count += 1
    
    def __del__(self):
        """Takes into account deletions of an employee instance."""
        __class__._employees_count -= 1
        print(f"employee '{self.name}' - {self.salary} is deleted. Now we have {__class__._employees_count} employees")

    @staticmethod
    def print_employees_count():
        """Prints active employees count."""
        print(f"There are {__class__._employees_count} active employees.")
    
    @staticmethod
    def print_employees(employees):
        """A method that displays information about each employee 
           in particular, namely the name and salary."""
        for e in employees:
            print(e)
    
    @staticmethod
    def print_base():
        """Displays information about the base classes
           from which the employee class is inherited (__base__)"""
        base = __class__.__base__
        print("Base classes list:")
        while base: 
            print(f"\t{base}")
            base = base.__base__

    @staticmethod
    def print_namespace():
        """Prints the class namespace."""
        print("The class namespace")
        for d in __class__.__dict__:
            print(f"\t{d}")

    @staticmethod
    def print_class_name():
        """Prints the class name (_name_)"""
        print(f"Class name: {__class__.__name__}")
    
    @staticmethod
    def print_module_name():
        """Prints the module name in which the class is defined (__mmodule__)"""
        print(f"Module name: {__class__.__module__}")
    
    @staticmethod
    def print_doc_bar():
        """Prints the documentation bar (_doc_)"""
        print(f"The doc bar: '{__class__.__doc__}'")
    
    @property
    def name(self):
        """Retuns the name of an employee. Read only."""
        return self._name
    
    @property
    def salary(self):
        """Retuns the salary of an employee."""
        return self._salary
    
    @salary.setter
    def salary(self, value: float):
        """Changes the salary of an employee."""
        if value < 0:
            raise ValueError("Salary can't be less than zero")
        self._salary = value

    def __str__(self):
        return f"The employee instance. {self.name = } {self.salary = }"

##############################
# e1 = employee("Basil", 123.45)
# e2 = employee("Pedro", 234.56)
# e3 = employee("Juan", 345.67)
# employee.print_employees_count()
# employee.print_employees([e1, e2, e3])
# print("----- deletion -----")
# del(e2)
# del(e3)
# employee.print_employees_count()
# employee.print_employees([e1])
# print("---------------")
# employee.print_base()
# employee.print_namespace()
# employee.print_class_name()
# employee.print_module_name()
# employee.print_doc_bar()
# print("----- end -----")