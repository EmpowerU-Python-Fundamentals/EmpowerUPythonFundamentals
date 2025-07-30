from abc import ABC, abstractmethod
from typing import List, Optional
import threading

# Abstract Base Class (Interface Segregation & Dependency Inversion)
class Shape(ABC):
    """Abstract base class for all shapes - demonstrates abstraction"""
    
    def __init__(self, name: str):
        self._name = name  # Encapsulation - protected attribute
    
    @property
    def name(self) -> str:
        """Getter for name - encapsulation"""
        return self._name
    @abstractmethod
    def calculate_area(self) -> float:
        """Abstract method - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def get_info(self) -> str:
        """Abstract method for getting shape information"""
        pass

# Polygon class implementing Shape interface
class Polygon(Shape):
    """Base polygon class - demonstrates inheritance and encapsulation"""
    
    def __init__(self, name: str, sides: int):
        super().__init__(name)  # Call parent constructor
        self._sides = sides  # Encapsulation - protected attribute
        self._validate_sides()
    
    def _validate_sides(self) -> None:
        """Private method for validation - encapsulation"""
        if self._sides < 3:
            raise ValueError("A polygon must have at least 3 sides")
    
    @property
    def sides(self) -> int:
        """Getter for sides - encapsulation"""
        return self._sides
    
    def get_info(self) -> str:
        """Implementation of abstract method - polymorphism"""
        return f"{self.name} is a polygon with {self.sides} sides"
    
    @abstractmethod
    def calculate_area(self) -> float:
        """Still abstract - to be implemented by concrete subclasses"""
        pass

# Rectangle class inheriting from Polygon
class Rectangle(Polygon):
    """Rectangle class - demonstrates inheritance and polymorphism"""
    
    def __init__(self, width: float, height: float):
        super().__init__("Rectangle", 4)  # Rectangle has 4 sides
        self._width = self._validate_dimension(width, "width")
        self._height = self._validate_dimension(height, "height")
    
    def _validate_dimension(self, value: float, dimension_name: str) -> float:
        """DRY principle - reusable validation method"""
        if value <= 0:
            raise ValueError(f"{dimension_name} must be positive")
        return value
    
    @property
    def width(self) -> float:
        """Getter for width - encapsulation"""
        return self._width
    
    @property
    def height(self) -> float:
        """Getter for height - encapsulation"""
        return self._height
    
    def calculate_area(self) -> float:
        """Implementation of abstract method - polymorphism"""
        return self._width * self._height
    
    def get_info(self) -> str:
        """Override parent method - polymorphism"""
        base_info = super().get_info()
        return f"{base_info} with width {self.width} and height {self.height}"

# Human class with proper encapsulation
class Human:
    """Human class demonstrating encapsulation and method types"""
    
    # Class variable (shared by all instances)
    species = "Homosapiens"
    
    def __init__(self, name: str):
        self._name = self._validate_name(name)  # Encapsulation
    
    def _validate_name(self, name: str) -> str:
        """Private validation method - encapsulation"""
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        return name.strip()
    
    @property
    def name(self) -> str:
        """Getter for name - encapsulation"""
        return self._name
    
    def display_welcome(self) -> str:
        """Instance method - displays welcome message"""
        return f"Welcome, {self.name}!"
    
    def get_species_info(self) -> str:
        """Instance method that returns species information"""
        return f"I am a member of the species: {self.species}"
    
    @staticmethod
    def get_arbitrary_message() -> str:
        """Static method - returns arbitrary message"""
        return "Humans are amazing creatures capable of great things!"
    
    def __str__(self) -> str:
        """String representation - polymorphism"""
        return f"Human(name='{self.name}')"

# Employee Manager Singleton (Single Responsibility + Singleton Pattern)
class EmployeeManager:
    """Singleton class for managing employees - demonstrates Singleton pattern"""
    
    _instance = None
    _lock = threading.Lock()  # Thread-safe singleton
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self._employees: List['Employee'] = []
            self._initialized = True
    
    def add_employee(self, employee: 'Employee') -> None:
        """Add employee to the system"""
        self._employees.append(employee)
    
    def get_total_employees(self) -> int:
        """Get total number of employees"""
        return len(self._employees)
    
    def get_all_employees(self) -> List['Employee']:
        """Get all employees"""
        return self._employees.copy()  # Return copy to maintain encapsulation

# Employee class demonstrating composition and dependency injection
class Employee:
    """Employee class demonstrating encapsulation and composition"""
    
    def __init__(self, name: str, salary: float, manager: Optional[EmployeeManager] = None):
        self._name = self._validate_name(name)
        self._salary = self._validate_salary(salary)
        
        # Dependency injection - if no manager provided, use singleton
        self._manager = manager or EmployeeManager()
        self._manager.add_employee(self)  # Register with manager
    
    def _validate_name(self, name: str) -> str:
        """DRY principle - reusable validation"""
        if not name or not isinstance(name, str):
            raise ValueError("Employee name must be a non-empty string")
        return name.strip()
    
    def _validate_salary(self, salary: float) -> float:
        """DRY principle - reusable validation"""
        if not isinstance(salary, (int, float)) or salary < 0:
            raise ValueError("Salary must be a non-negative number")
        return float(salary)
    
    @property
    def name(self) -> str:
        """Getter for name - encapsulation"""
        return self._name
    
    @property
    def salary(self) -> float:
        """Getter for salary - encapsulation"""
        return self._salary
    
    @salary.setter
    def salary(self, value: float) -> None:
        """Setter for salary with validation - encapsulation"""
        self._salary = self._validate_salary(value)
    
    def get_employee_info(self) -> str:
        """Get employee information"""
        return f"Employee: {self.name}, Salary: ${self.salary:,.2f}"
    
    def __str__(self) -> str:
        """String representation"""
        return f"Employee(name='{self.name}', salary={self.salary})"
    
    def __repr__(self) -> str:
        """Developer representation"""
        return self.__str__()

# Report Generator class (Single Responsibility Principle)
class EmployeeReportGenerator:
    """Handles employee reporting - demonstrates Single Responsibility"""
    
    def __init__(self, manager: EmployeeManager):
        self._manager = manager
    
    def print_total_employees(self) -> None:
        """Print total number of employees"""
        total = self._manager.get_total_employees()
        print(f"Total number of employees: {total}")
    
    def display_all_employees(self) -> None:
        """Display information about all employees"""
        employees = self._manager.get_all_employees()
        if not employees:
            print("No employees found.")
            return
        
        print("\n=== Employee Information ===")
        for i, employee in enumerate(employees, 1):
            print(f"{i}. {employee.get_employee_info()}")
    
    def generate_class_info_report(self) -> None:
        """Display comprehensive class information"""
        print("\n=== Employee Class Information ===")
        print(f"Base classes: {Employee.__bases__}")
        print(f"Class namespace (__dict__ keys): {list(Employee.__dict__.keys())}")
        print(f"Class name (__name__): {Employee.__name__}")
        print(f"Module name (__module__): {Employee.__module__}")
        print(f"Documentation (__doc__): {Employee.__doc__}")