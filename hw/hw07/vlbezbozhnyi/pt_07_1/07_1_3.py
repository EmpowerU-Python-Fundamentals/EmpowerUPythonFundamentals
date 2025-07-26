def count_characters(string: str) -> dict:
    """
    Calculate the number of characters in a string.
    """
    char_dict = {}

    for char in string:
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1

    return char_dict
