def letter_calc(word):
    """This function counts number of letters"""
    letter_d = dict()
    for i in word:
        letter_d[i] = word.count(i)
    return letter_d


num_of_letter = input("Enter any word: ").lower()
print(letter_calc(num_of_letter))