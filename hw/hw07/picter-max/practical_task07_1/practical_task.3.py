def my_function(word: str):
    out_dict = dict()
    lower_word = word.lower()
    for characters in lower_word:
        if not characters in out_dict:
            out_dict[characters] = lower_word.count(characters)
    return out_dict

word = input('your word: ')
print(my_function(word))