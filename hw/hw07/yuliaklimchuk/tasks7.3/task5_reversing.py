# You need to write a function that reverses the words in a given string. 
# Words are always separated by a single space.
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

def reverse(st):
    words = st.split()
    words.reverse()
    return ' '.join(words)

