# Task1. Write a function that returns the largest number of two numbers
# (use DocStrings documentation strings in the function)
def get_largest_number(a, b):
    """This function returns the largest number of two numbers"""
    return a if a>b else b
		
# Task3. Write a function that calculates the number of characters included in given string
#my_str="hello"
def calculate_number_of_characters(str):
    my_dict= {}
    for i in str:
        if my_dict.get(i) is None:
            my_dict.update({i:1})
        else:
            my_dict.update({i:my_dict.get(i)+1})
    return my_dict