def largest(a, b):
    """Return the largest number.
    
    a is the first number.
    b is the second number.
    
    This function returns the bigger number."""
    
    return a if a > b else b
    
def main():
    print("Enter 2 numbers:")
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    print(f"This number is bigger: {largest(first, second)}")
    
# Run the program
main()