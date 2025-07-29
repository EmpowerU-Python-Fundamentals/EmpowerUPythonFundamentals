# Code written by Ivan Savytsky
# Code reviewed for PEP 8 compliance by ChatGPT

def greet(name):
    """Return a greeting for Johnny or any other name."""
    if not isinstance(name, str):
        return "Invalid input. Please enter a name as text."

    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

def main():
    """Demonstrate the greet() function."""
    print(greet("Johnny"))       # Output: Hello, my love!
    print(greet("Jenny"))        # Output: Hello, Jenny!
    print(greet(123))            # Output: Invalid input. Please enter a name as text.


if __name__ == "__main__":
    main()
