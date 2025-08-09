def char_count(text):
    """
    Returns:
        dict: A dictionary with characters as keys and their counts as values.
    Parameters:
        text (str): Input string.
   
    """
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts

# Example usage:
print(char_count("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(char_count("character"))  # {'c': 2, 'h': 1, 'a': 1, 'r': 2, 't': 1, 'e': 1}
print(char_count("Python programming"))  # {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, ' ': 1, 'p': 1, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1}