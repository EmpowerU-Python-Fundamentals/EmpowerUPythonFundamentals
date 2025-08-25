def reverse(st):
    """
    Reverse a string, delete all trailing spaces
    """
    words = st.strip().split(" ")
    return " ".join(reversed(words))

#Test:
print(reverse('Hello World'))
print(reverse('Hi There.'))