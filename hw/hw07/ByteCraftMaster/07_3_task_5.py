# You need to write a function that reverses the words in a given string. Words are always separated by a single space.
# As the input may have trailing spaces, you will also need to ignore unnecessary whitespace.

def reverse(st):
    list = st.split()
    list.reverse()
    return " ".join(list)