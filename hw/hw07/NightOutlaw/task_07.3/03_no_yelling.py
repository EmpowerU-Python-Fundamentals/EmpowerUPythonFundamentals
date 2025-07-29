def filter_words(st):
    words = st.split()
    normalized = [word.lower() for word in words]
    normalized[0] = normalized[0].capitalize()
    return ' '.join(normalized)
