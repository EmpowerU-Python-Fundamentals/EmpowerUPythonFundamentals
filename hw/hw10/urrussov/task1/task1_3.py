class Employee:
    count = 0
    def __init__(self,name,salary):
        Employee.count += 1
        self.name = name
        self.salary = salary
    @classmethod
    def emp_count(cls):
        """Returns the current count of Employee instances."""
        return cls.count
    def intro_each_employee(self):
        """Prints a welcome message for the employee, displaying their name and salary."""
        print(f'\nWelcome {self.name}! Your salary is {self.salary}$\n') 

def add_name_new_emp():
    """
    Prompts the user to input an employee's first name and surname, validating that both consist of letters only.
    Continues to prompt until valid inputs are provided for both fields.
    """
    while True:
        n = input('Write employee`s name: ')
        if n.isalpha():
            break
        else:
            print("You didn't write a valid name. Try again (letters only).")
    while True:
        s = input('Write employee`s surname: ')
        if s.isalpha():
            break
        else:
            print("You didn't write a valid surname. Try again (letters only).")
    full_n = n + " " + s
    return full_n

def add_salary_new_employee():
    """
    Prompts the user to input an employee's salary, ensuring the input is a valid integer.
    The function repeatedly asks the user to enter a salary value until a valid integer is provided.
    If the input is not a digit, it displays an error message and prompts again.
    """
    while True:
        m = input('Write employee`s salary: ')
        if m.isdigit():
            m = int(m)
            break
        else:
            print("You didn't enter a valid salary. Please enter digits only.")
    return m

def print_menu():
    print("\nSelect:")
    print("1 - Add new employee")
    print("2 - Print amount")
    print("3 - All employees")
    print("4 - Info about the base classes")
    print("5 - Quit")

emp_dict = {}

def main_logic():
    while True:
        try:
            print_menu()
            choice = int(input("Your choice?: "))
        except ValueError:
            print("Please enter a valid number from the menu.")
            continue

        match choice:
            case 1:
                name_new = add_name_new_emp()
                salary_new = add_salary_new_employee()
                new = Employee(name_new, salary_new)
                new.intro_each_employee()
                emp_dict[name_new] = salary_new

            case 2:
                print(f'\nThe amount of employees is {Employee.emp_count()}\n')

            case 3:
                if emp_dict:
                    print("\nAll employees:")
                    for key, value in emp_dict.items():
                        print(f" - {key}: {value}$")
                else:
                    print("\nNo employees added yet.")

            case 4:
                print("\nBase class:", Employee.__base__)
                print("\nNamespace (__dict__):")
                for key in Employee.__dict__:
                    print(f" - {key}")
                print("\nClass name:", Employee.__name__)
                print("Module name:", Employee.__module__)
                print("\nDocstring:")
                print(Employee.__doc__)

            case 5:
                print("\nProgram ended. Goodbye!")
                break

            case _:
                print("Please choose a valid option (1–4).")

if __name__ == '__main__':
    main_logic()