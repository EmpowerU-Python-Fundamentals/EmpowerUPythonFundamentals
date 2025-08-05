from student import Student, StudentError
from log import logging
# --- Example Usage ---

# This list contains both valid and invalid student data to demonstrate error handling.
student_data = [
    ("Alice", 21),       # Valid data
    ("Bob", 19),         # Valid data
    ("", 20),            # Invalid name
    ("Charlie", -5),     # Invalid age
    ("Diana", "22")      # Invalid age type
]

# We will iterate through the data and create a Student object for each valid entry.
print("Attempting to create Student objects:")

for name, age in student_data:
    logging.debug(f"for iter {name=} {age=}")
    try:
        # Attempt to create a new Student object.
        student = Student(name, age)
        print(f"\nSuccessfully created student: {student.name}")
        student.display_info()
    except StudentError as e:
        # Catch our custom StudentError and print a friendly message.
        logging.error(f"Failed to create student with name='{name}', age='{age}'.")
        print(f"Error: {e}")
