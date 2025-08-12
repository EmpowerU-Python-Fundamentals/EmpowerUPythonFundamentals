def number_of_characters(text: str):
    result = {}
    for char in text:
        result[char] = result.get(char, 0) + 1
    return result
