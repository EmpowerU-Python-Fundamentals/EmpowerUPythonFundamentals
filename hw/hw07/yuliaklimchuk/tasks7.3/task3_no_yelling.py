# Write a function taking in a string like WOW this is REALLY          amazing and
# returning Wow this is really amazing. String should be capitalized and properly spaced. 
# Using re and string is not allowed.

def filter_words(st):
    words = st.split()
    words_lower = []
    for word in words:
        words_lower.append(word.lower())
    words_lower[0] = words_lower[0].capitalize()
    return ' '.join(words_lower)



