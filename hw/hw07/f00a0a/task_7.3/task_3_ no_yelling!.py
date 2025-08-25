def filter_words(st):
    words = st.split()  
    cleaned = " ".join(words)  
    cleaned = cleaned.lower()
    return cleaned.capitalize() 
print(filter_words("WOW this is REALLY          amazing"))