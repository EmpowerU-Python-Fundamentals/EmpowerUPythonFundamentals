def characters_counter(s):
    """
    Returns a dictionary with the count of each character in the given string.

    Parameters:
    s (str): The input string.

    Returns:
    dict: A dictionary where keys are characters and values are their counts.
    """
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

if __name__ == '__main__':
    print(characters_counter("hello"))
