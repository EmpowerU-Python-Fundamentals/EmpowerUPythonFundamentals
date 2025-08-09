# --- Task 3: Calculate the number of characters in a string ---
# This function counts the occurrences of each character in a given string.
def count_characters(input_string):
    """
    Calculates the number of times each character appears in a string.

    Args:
        input_string (str): The string to analyze.

    Returns:
        dict: A dictionary where keys are characters and values are their counts.
    """
    char_count = {}
    for char in input_string:
        # If the character is already in the dictionary, increment its count.
        if char in char_count:
            char_count[char] += 1
        # Otherwise, add the character to the dictionary with a count of 1.
        else:
            char_count[char] = 1
    return char_count

print("--- Running Task 3 ---")
input_str = "hello"
print(f"The character count for '{input_str}' is: {count_characters(input_str)}")
input_str_2 = "softserve"
print(f"The character count for '{input_str_2}' is: {count_characters(input_str_2)}")
