def filter_words(text):
    if not text:
        return text

    words = [word for word in text.split() if word]

    formatted_words = []
    for i, word in enumerate(words):
        if i == 0:
            formatted_words.append(word[0].upper() + word[1:].lower())
        else:
            formatted_words.append(word.lower())

    return ' '.join(formatted_words)