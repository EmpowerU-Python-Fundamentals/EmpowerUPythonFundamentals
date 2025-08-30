def get_number_characters(word: str):
    """This function calculates number of characters in given string."""
    str_list = list(word)
    word_dictionary = dict.fromkeys(str_list, 0)
    for letter in str_list:
        word_dictionary[letter] += 1
    return word_dictionary

print(get_number_characters("hello"))