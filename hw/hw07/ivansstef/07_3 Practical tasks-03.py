# Code written by Ivan Savytsky
# Code reviewed for PEP 8 compliance by ChatGPT


def filter_words(sentence):
    """Return sentence with proper spacing and capitalization."""
    if not isinstance(sentence, str):
        return "Please enter a string."

    words = sentence.strip().split()
    sentence_clean = " ".join(words).lower()
    return sentence_clean.capitalize()


def main():
    print(filter_words("  WOW this is REALLY          amazing"))
    print(filter_words(123))  # Invalid


if __name__ == "__main__":
    main()
