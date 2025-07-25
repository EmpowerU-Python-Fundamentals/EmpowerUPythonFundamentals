def characters_frequency(string):
    """
    Function calculates the number of characters included in given string

    Parameters:
    string (str): Input string.

    Returns:
    dict: Dictionary where keys are characters and values are their amounts.
    """

    characters_frequency = {}
    for character in string:        
        characters_frequency[character] = characters_frequency.get(character, 0)+1        
    return characters_frequency