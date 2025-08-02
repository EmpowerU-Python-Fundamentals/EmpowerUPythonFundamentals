def filter_words(st):
    """
    Capitalize a string and remove all unecessary spaces
    """
    cap = st.capitalize()
    return ' '.join(cap.split())

#Test:
print(filter_words('HELLO world!'))
print(filter_words('This    will    not    pass '))
print(filter_words('NOW THIS is a VERY EXCITING test!'))