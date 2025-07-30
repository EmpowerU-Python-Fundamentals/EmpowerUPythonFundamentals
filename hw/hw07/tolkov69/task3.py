def count_characters(input_string):
   
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

print(count_characters("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
