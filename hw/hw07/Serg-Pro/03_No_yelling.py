def filter_words(st):
    # Remove extra spaces and split into words
    words = st.split()
    
    # Convert all words to lowercase
    words = [word.lower() for word in words]
    
    # Capitalize the first word
    if words:
        words[0] = words[0].capitalize()
    
    # Join the words into a sentence
    return ' '.join(words)
