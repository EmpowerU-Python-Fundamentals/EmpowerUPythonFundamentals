#Напишіть функцію, яка обчислює кількість символів у заданому рядку.
#- вхідні дані: "hello"
#- вихідні дані: {"h":1, "e":1, "l":2, "o":1}
def char_count(input_string):
    char_counts = {}
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

text = input("Введіть рядок: ")
print(char_count(text))