def count_chars(s):
    """
    Calculates the number of each character in a string.
    Args:
        s (str): Input string.
    Returns:
        dict: Dictionary with character counts.
    """
    return {char: s.count(char) for char in set(s)}

# Тест
if __name__ == "__main__":
    print(count_chars("hello"))  # {'h':1, 'e':1, 'l':2, 'o':1}
