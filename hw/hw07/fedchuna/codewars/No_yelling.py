def filter_words(st):
    words = st.lower().split()
    processed_string = " ".join(words)
    return processed_string.capitalize()