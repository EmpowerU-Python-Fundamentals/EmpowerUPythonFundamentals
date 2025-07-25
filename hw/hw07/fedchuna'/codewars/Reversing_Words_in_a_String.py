def reverse(st):
    words = st.split()
    reversed_words = words[::-1]
    st = " ".join(reversed_words)
    return st