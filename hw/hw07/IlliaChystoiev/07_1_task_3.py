# Task3. Write a function that calculates the number of characters included in given string
#   input: "hello"
#   output: {"h":1, "e":1,"l":2,"o":1}


def char_count(input: str) -> dict:
    output = {}
    for i in input:
        output[i] = output.get(i, 0) + 1
    print(output)
    # return output # - uncomment this line to return the output

input = "hello"
char_count(input)
