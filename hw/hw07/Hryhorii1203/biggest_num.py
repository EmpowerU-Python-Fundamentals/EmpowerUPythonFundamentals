def find_largest(a, b):
    """
    Returns the largest of two numbers.    
    Args:
        a (int/float): First number.
        b (int/float): Second number.
    Returns:
        int/float: The larger number.
    """
    return max(a, b)
if __name__ == "__main__":
    print(find_largest(5, 10)) 
