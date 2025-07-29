def calculate_char(text):
    """
    Calculate the number of characters in the string.

    text (str): The input string.

    dict: A dictionary with characters as keys and their counts as values.
    """
    result = {}
    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result
    
def main():
    string = input("Enter a string: ")
    print(f"Number of characters: {calculate_char(string)}")
    
# Run the program
main()