def character_count(text):
    """The function counts the number of occurrences of a character in a string"""

    text_edit = text.lower().strip()
    char_dict = {}
    for letter in text_edit:
        count = text_edit.count(letter)
        char_dict[f'{letter}'] = count

    return char_dict

text = input("Input text \n")
print(character_count(text))
