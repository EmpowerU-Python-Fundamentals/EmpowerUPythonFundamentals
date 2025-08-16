class Employee:
    """
    A class representing an employee.
    Has a counter for the total number of employees.
    """
    COUNTER = 0

    def __init__(self, name, salary):
        """
        Constructor for the Employee class.
        Increments the employee counter.
        
        Arguments:
            name (str): Employee's name.
            salary (float): Employee's salary.
        """
        self.__name = name
        self.__salary = salary
        Employee.COUNTER += 1

    def __del__(self):
        """
        Destructor for the Employee class.
        Decrements the employee counter when an object is deleted.
        """
        Employee.COUNTER -= 1

    @staticmethod
    def get_num_of_employees():
        """
        A static method that prints the current number of employees.
        """
        print(f"Total number of employees: {Employee.COUNTER}")

    def show_employee_info(self):
        """
        A method that prints information about a specific employee.
        """
        print(f'Name: {self.name}, Salary: {self.salary}')

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary


# Example usage
if __name__ == "__main__":
    emp1 = Employee('Anna', 1500.0)
    emp2 = Employee('Boryslav', 1200.0)
    
    Employee.get_num_of_employees()
    emp1.show_employee_info()
    emp2.show_employee_info()

    print("-" * 20)
    print("Deleting object emp2...")
    del emp2
    
    Employee.get_num_of_employees()
    print("-" * 20)

    # Output of special class attributes
    print(f"__base__: {Employee.__base__}")
    print(f"__dict__: {Employee.__dict__}")
    print(f"__name__: {Employee.__name__}")
    print(f"__module__: {Employee.__module__}")
    print(f"__doc__: {Employee.__doc__}")
