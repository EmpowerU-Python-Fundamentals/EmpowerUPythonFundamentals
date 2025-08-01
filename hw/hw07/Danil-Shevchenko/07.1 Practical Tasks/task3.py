def char_in_string(string):
    """
    Calculates the number of characters included in given string  
    """
    res = {}
    
    for char in string:
        if char in res:
            res[char] += 1
        else:
            res[char] = 1
    return res

input_str = "hello"
print(char_in_string(input_str))    
input_str = "world"
print(char_in_string(input_str))    
input_str = "hello world"
print(char_in_string(input_str))    
