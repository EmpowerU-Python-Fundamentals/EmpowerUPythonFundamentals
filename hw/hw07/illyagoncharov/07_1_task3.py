def char_counter(string):
    """The function takes a string and returns a dictionary in the form
    {character: its number in the string, }"""
    return {i:string.count(i) for i in string}


