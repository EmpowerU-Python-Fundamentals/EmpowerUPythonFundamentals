import math

AREAS = {
    "rectangle": lambda a, b: a * b,
    "triangle": lambda a, b, c: math.sqrt((s := (a + b + c) / 2) \
                                          * (s - a) * (s - b) * (s - c)),
    "circle": lambda r: 3.14 * r**2,
}

def main():
    """
    Handles user input and displays the calculated area.
    Keeps asking for input until valid numbers are provided.
    """
    while True:
        user_input = input("Enter numbers (or 'exit'): ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        try:
            area = get_area(user_input)
            print(f"Area: {area:.2f}")
        except (TypeError, ValueError) as e:
            print(f"Error: {e}")


def data_validator(m_func):
    """
    A decorator that checks if input strings are valid numbers.
    Raises a TypeError if not all parts of the string are numbers.
    """

    def wrapper(str_nm):
        data = (is_float(n) for n in str_nm.split())
        data_len = len(list(data))

        if not all(data):
            raise TypeError("Data must be an number")
        elif not ( 0 < data_len < 4):
            raise ValueError("Data must be between 0 and 4")
        elif data_len == 3:
            a_side, b_side, c_dside = get_float(str_nm)
            if a_side > b_side + c_dside or \
                    b_side > a_side + c_dside or \
                    c_dside > a_side + b_side:
                raise ValueError("Its not a triangle")

        return m_func(str_nm)
    return wrapper

def is_float(num_str):
    """
    Checks if a string can be converted to a floating-point number.
    """

    try:
        float(num_str)
        return True
    except ValueError:
        return False

@data_validator
def get_area(str_nm):
    """
    Calculates the area based on the number of inputs:
    - 1 number: circle area
    - 2 numbers: rectangle area
    - 3 numbers: triangle area
    """

    nums = list(map(float, str_nm.split()))
    sides_num = len(nums)

    match sides_num:
        case 1:
            return AREAS["circle"](*nums)
        case 2:
            return AREAS["rectangle"](*nums)
        case 3:
            return AREAS["triangle"](*nums)
    return None

@data_validator
def get_max(num_a, num_b):
    """Returns the larger of two numbers."""
    return max(num_a, num_b)

def count_chars(text):
    """Counts the occurrences of each character in a string."""
    return {c: text.count(c) for c in text}

def get_float(num_str):
    return list(map(float, num_str.split()))

if __name__ == "__main__":
    main()
