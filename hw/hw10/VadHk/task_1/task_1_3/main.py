from classes.employee import Employee

def main():
    employee_1 = Employee("John Doe", 50000)
    print(employee_1.employee_info())

    employee_2 = Employee("David Abrahaam", 30000)
    print(employee_2.employee_info())

    employee_3 = Employee("Jane Finger", 10000)
    print(employee_3.employee_info())

    Employee.get_counter()

    employee_1.class_info()

if __name__ == "__main__":
    main()