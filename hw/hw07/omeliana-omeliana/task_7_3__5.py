def reverse(st):
    """Reversing Words in a String"""
    text = st.split()
    text.reverse()
    st = " ".join(text)
    return st