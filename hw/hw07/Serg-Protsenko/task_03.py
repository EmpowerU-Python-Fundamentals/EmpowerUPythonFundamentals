def count_characters(s):
    """
    Count the number of occurrences of each character in a string.

    Parameters:
    s (str): Input string

    Returns:
    dict: Dictionary with characters as keys and their counts as values
    """
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    return result

print(count_characters(input("Input your word: ")))
