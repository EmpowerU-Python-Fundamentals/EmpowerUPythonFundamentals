def get_count_characters(string: str) -> dict:
    """
    Counts the number of occurrences of each character in a given string.
    """
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

input_str = "hello"
print(get_count_characters(input_str))