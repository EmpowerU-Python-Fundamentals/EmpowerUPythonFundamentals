def reverse_string(word):
    return ' '.join(word.strip().split()[::-1])

print(reverse_string("Hello World"))
print(reverse_string("Hi There."))
