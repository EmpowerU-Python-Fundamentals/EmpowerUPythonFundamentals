# The StudentError class is a custom exception that inherits from Python's built-in Exception class.
# We create this to handle specific errors related to student data,
# making our error handling more descriptive and organized.

from log import logging


class StudentError(Exception):
    """
    A custom exception for handling errors specific to the Student class.
    """
    def __init__(self, message):
        super().__init__(message)
        self.message = message

# The Student class represents a student with a name and age.
# It includes data validation in its constructor.
class Student:
    """
    Represents a student with a name and age.
    Raises StudentError for invalid data.
    """
    def __init__(self, name, age):
        # Validate that the name is a non-empty string.
        if not isinstance(name, str) or not name:
            logging.error("Student name must be a non-empty string.")
            raise StudentError("Student name must be a non-empty string.")

        # Validate that the age is an integer greater than 0.
        if not isinstance(age, int) or age <= 0:
            logging.error("Student age must be a positive integer.")
            raise StudentError("Student age must be a positive integer.")

        self.name = name
        self.age = age
        logging.info(f"create student ")

    def display_info(self):
        """
        Prints the student's name and age.
        """
        logging.debug(f"display_info for {self}")
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")
