def reverse_words(s):
    words = s.strip().split()  # Remove leading/trailing spaces and split into words
    return ' '.join(reversed(words))

print(reverse_words("Hello World"))
print(reverse_words("Hi There."))
print(reverse_words("   Happy coding!   "))