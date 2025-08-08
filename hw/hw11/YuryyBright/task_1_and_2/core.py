import logging
from abc import ABC, abstractmethod
from typing import Optional

class Logger:
    _instance = None
    
    def __new__(cls, name: str= 'main', level:int = logging.INFO):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._setup_logger(name, level)
        return cls._instance
    
    def _setup_logger(self, name:str, level: int):
        """Set up and configure a logger with the specified name and level."""
        
        self.logger = logging.getLogger(name)
        if not self.logger.handlers:  # Avoid adding multiple handlers
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(level)

    def get_logger(self):
        return self.logger

class Processor(ABC):
    
    @abstractmethod
    def process(self, input_data:str):
        """_summary_

        Args:
            input_data (str): _description_
        """
        pass

class AgeProcessor(Processor):
    __slots__ = ('logger', )
    def __init__(self):
        self.logger = Logger(__name__).get_logger()
        
    def process(self, age):
        try:
            age = int(age)
            
            if age == 0:
                raise ValueError("Age cannot be zero")
            elif age < 0:
                raise ValueError("Age cannot be negative")
            return "even" if age % 2 == 0 else "odd"
        except ValueError as e:
            self.logger.error(f"Invalid input: {e}")
            return str(e)
        
class DayProcessor:
    __slots__ = ('logger', 'days')
    def __init__(self):
        self.logger = Logger(__name__).get_logger()
        self.days = {
            1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday",
            5: "Friday", 6: "Saturday", 7: "Sunday"
        }

    def process(self, number: str) -> str:
        """Process day number input and return the corresponding day."""
        try:
            number = int(number)
            if number < 1 or number > 7:
                return "Number out of range (1-7)"
            return self.days.get(number, "Invalid day")
        except ValueError:
            self.logger.error("Non-numerical input provided")
            return "Please enter a valid number"

class ProcessorManager:
    __slots__ = ('age_processor', 'day_processor')
    
    def __init__(self, AgeProcessor_: AgeProcessor = AgeProcessor, DayProcessor_: DayProcessor = DayProcessor):
        self.age_processor = AgeProcessor_()
        self.day_processor = DayProcessor_()
    
    def process_age(self, age: str) -> tuple[str, bool]:
        """Process age and return result with validity flag."""
        result = self.age_processor.process(age)
        is_valid = result in ["even", "odd"]
        return result, is_valid

    def process_day(self, day_num: str) -> tuple[str, bool]:
        """Process day number and return result with validity flag."""
        result = self.day_processor.process(day_num)
        is_valid = result in self.day_processor.days.values()
        return result, is_valid