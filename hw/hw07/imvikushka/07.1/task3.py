# Task 3. Write a function that calculates the number of characters included in given string.

def count_characters(string):
    char_counts = {}
    
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts