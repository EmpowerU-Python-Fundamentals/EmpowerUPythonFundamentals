def count_characters(input_string):
    a = set(input_string)
    d = dict()
    for char in a:
        if char.isalpha():
            d[char] = input_string.count(char)
        elif char.isdigit():
            d[char] = input_string.count(char)
        else:
            d[char] = input_string.count(char)
    return d

    
    

user_input = input("Enter a string: ")
print(count_characters(user_input))