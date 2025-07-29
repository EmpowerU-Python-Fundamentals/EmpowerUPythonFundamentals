def reverse(st):
    # Split the string into words (automatically handles extra spaces)
    words = st.strip().split()
    
    # Reverse the list of words
    reversed_words = words[::-1]
    
    # Join them back into a single string with single spaces
    return ' '.join(reversed_words)
