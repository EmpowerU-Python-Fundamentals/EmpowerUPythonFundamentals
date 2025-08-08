def filter_words(st):
    return " ".join(st.split()).capitalize()

print(filter_words("WOW this is REALLY          amazing"))  # Output: "Wow this is really amazing"