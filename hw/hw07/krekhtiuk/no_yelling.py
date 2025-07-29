def filter_words(text):
    return " ".join(text.strip().split()).lower().capitalize()
print(filter_words("WOW this is REALLY          amazing"))
