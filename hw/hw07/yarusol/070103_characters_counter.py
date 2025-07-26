# Task3.
# Write a function that calculates the number of characters
# included in given string

def count_characters(text: str):
    characters = {}
    keys = characters.keys()
    for ch in text:
        if ch not in keys:
            characters[ch] = 1
        else:
            characters[ch] += 1

    return characters

# main
# text = input("Input your string: ")
# print(f"counted characters are: {count_characters(text)}")