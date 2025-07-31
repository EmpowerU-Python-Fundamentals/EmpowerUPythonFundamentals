def filter_words(st):
    s = st.lower()
    words = s.split()
    cleaned = ' '.join(words)
    result = cleaned.capitalize()
    
    return result