# You need to write a function that reverses the words in a given string.
# Words are always separated by a single space.
# As the input may have trailing spaces,
#   you will also need to ignore unneccesary whitespace.

def reverse(st: str):
    words = reversed(list(filter(lambda w: w, [w for w in st.split(" ")])))
    st = " ".join(words)
    return st

print(f"{reverse("Hello World") = }") # --> "World Hello"
print(f"{reverse("Hi There.") = }") # --> "There. Hi"