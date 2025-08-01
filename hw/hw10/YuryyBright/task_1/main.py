from core import Rectangle, Human, Employee, EmployeeManager, EmployeeReportGenerator

# Demonstration function
def demonstrate_all_principles():
    """Demonstrate all OOP principles and patterns"""
    
    print("=== HOMEWORK SOLUTION DEMONSTRATION ===\n")
    
    # Task 1: Polygon and Rectangle
    print("TASK 1: Polygon and Rectangle Classes")
    print("-" * 40)
    try:
        rectangle = Rectangle(5.0, 3.0)
        print(f"Rectangle info: {rectangle.get_info()}")
        print(f"Rectangle area: {rectangle.calculate_area()} square units")
    except Exception as e:
        print(f"Error: {e}")
    
    # Task 2: Human class
    print(f"\nTASK 2: Human Class")
    print("-" * 40)
    try:
        person = Human("Alice")
        print(person.display_welcome())
        print(person.get_species_info())
        print(f"Static message: {Human.get_arbitrary_message()}")
        print(f"Human object: {person}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Task 3: Employee class and management
    print(f"\nTASK 3: Employee Class and Management")
    print("-" * 40)
    try:
        # Create employees
        emp1 = Employee("John Doe", 50000)
        emp2 = Employee("Jane Smith", 60000)
        emp3 = Employee("Bob Johnson", 55000)
        
        # Get manager instance (singleton)
        manager = EmployeeManager()
        
        # Create report generator
        report_gen = EmployeeReportGenerator(manager)
        
        # Display reports
        report_gen.print_total_employees()
        report_gen.display_all_employees()
        report_gen.generate_class_info_report()
        
        # Demonstrate singleton pattern
        manager2 = EmployeeManager()
        print(f"\nSingleton test - Same instance? {manager is manager2}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Demonstrate polymorphism
    print(f"\nPOLYMORPHISM DEMONSTRATION")
    print("-" * 40)
    shapes = [Rectangle(4, 5), Rectangle(2, 3)]
    for shape in shapes:
        print(f"{shape.get_info()} - Area: {shape.calculate_area()}")

if __name__ == "__main__":
    demonstrate_all_principles()