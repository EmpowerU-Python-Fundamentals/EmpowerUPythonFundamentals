def filter_words(st):
    """No yelling!"""
    text = st.strip()
    st = ' '.join(text.split())
    return st.capitalize()