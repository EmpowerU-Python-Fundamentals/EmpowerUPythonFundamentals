"""calculates letters"""
def calculates_letters(word: str) -> dict:
    """calculates the number of characters included in given string
    Args:
        word (str): word

    Returns:
        dict: dictionary with all letters calculated
    """
    sett = set()
    dictionary = {}
    for letter in word:
        if letter in sett:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
        sett.add(letter)
    return dictionary

your_word = input()
print(calculates_letters(your_word))
