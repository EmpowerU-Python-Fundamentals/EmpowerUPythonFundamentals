def reverse_words(string: str) -> str:
    words = string.split()
    return " ".join(words[::-1])


print(reverse_words("Hello World"))
print(reverse_words("Hi There."))
