def count_characters(string):
    return {char: string.count(char) for char in set(string)}

text = input("Enter text: ")
print(count_characters(text))