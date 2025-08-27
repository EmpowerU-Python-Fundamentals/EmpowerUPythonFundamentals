#TASK 1
class Polygon:
    def __init__(self):
        pass

class Rectangle(Polygon):
  def __init__(self, width, height):
      self.width = width
      self.height = height
      
  def area(self):
      return self.width * self.height

#TASK 2
class Human:
    human_species = "\"Homosapiens\""

    def __init__(self, name):
        self.name = name
        
    def greet(self):
        print ("Hello, I am {}.".format(self.name))
    
    def species (cls):
        print (f"I belong to {cls.human_species}")
    
    @staticmethod
    def message():
        print ("This is a Human class.")
   
#TASK 3
class Employee:
    total_employees = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def show_count(cls):
        """Display total number of employees"""
        print(f"Total number of employees: {cls.total_employees}")

    def show_employee(self):
        """Display info about a single employee"""
        print(f"Name: {self.name}, Salary: {self.salary}")


emp1 = Employee("Andrii", 50000)
emp2 = Employee("Liudmyla", 60000)

# Display individual employee info
emp1.show_employee()
emp2.show_employee()

# Display total number of employees
Employee.show_count()

print("\n--- Class Information ---")
print("Base classes:", Employee.__base__)
print("Namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Docstring:", Employee.__doc__)