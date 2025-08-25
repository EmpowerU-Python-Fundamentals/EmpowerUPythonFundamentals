def count_characters(s):
    """
    Counts the number of occurrences of each character in a string
    """
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

#Test:
print(count_characters("python"))
print(count_characters("ooooops"))
