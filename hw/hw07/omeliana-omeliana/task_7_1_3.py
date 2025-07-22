def string_characters(input_string):
    """Calculate the number of characters"""
    output = {}
    for i in input_string:
        if i in output:
            output[i] += 1
        else:
            output[i] = 1
    return output

input_string = input("Enter your string:\n")
output = string_characters(input_string)
print(output)
