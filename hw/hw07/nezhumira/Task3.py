def count_characters(text: str) -> dict:
    """
    Calculates the number of times each character appears in the given string.

    Parameters:
    text (str): The input string to analyze.

    Returns:
    dict: A dictionary with characters as keys and their counts as values.
    """
    result = {}
    for char in text:
        result[char] = result.get(char, 0) + 1
    return result

#print(count_characters("АБАБА-ГАЛА-МАГА"))