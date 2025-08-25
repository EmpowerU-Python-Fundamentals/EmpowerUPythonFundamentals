#TASK3

def num_of_char(string):
    char_dict ={}
    for ch in string:
        char_dict[ch] = char_dict.get(ch, 0) + 1
    return char_dict
print(num_of_char("hello hello"))    