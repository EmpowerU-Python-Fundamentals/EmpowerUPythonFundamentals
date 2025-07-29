def char_count(string):
    """Calculate the number of chars included in string"""
    result = {}
    for char in string:
        result[char] = result.get(char, 0) + 1
    return print(result)


word = "hello"
char_count(word)
