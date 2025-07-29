def reversing_word(word):
    word = word.strip().split()
    return " ".join(reversed(word))
print(reversing_word("Hello World"))
print(reversing_word("Hi There"))
