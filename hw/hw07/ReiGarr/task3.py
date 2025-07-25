def count_characters(s):
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

text = input('Enter string ')
print(count_characters(text))
