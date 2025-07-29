def get_count_symbols(enter_string):
    """
    Get dictionary with counts of each symbol in string.

    Args:
        enter_string (str): User input string

    Returns:
        dict: Dictionary with symbol countsG
    """

    # unique_symbols  = set(enter_string)
    # return {s: enter_string.count(s) for s in unique_symbols}
    char_count = {}
    for s in enter_string:
        char_count[s] = char_count.get(s, 0) + 1
    return char_count

if __name__ == "__main__":
    print(get_count_symbols("hello"))