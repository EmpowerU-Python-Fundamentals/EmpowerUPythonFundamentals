#07.1.3 Write a function that calculates the number of characters included in given string
# input: hello
# output: {"h":1,"e":1,"l":2,"0":1}

def count_chars(s):
    result = {}
    for ch in s:
        result[ch] = result.get(ch, 0) + 1
    return result

print(count_chars("hello"))