# Code written by Ivan Savytsky
# Code reviewed for PEP 8 compliance by ChatGPT


def reverse(sentence):
    """Reverse the order of words in the sentence."""
    if not isinstance(sentence, str):
        return "Please enter a string."

    words = sentence.strip().split()
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence


def main():
    print(reverse("Hello World"))     # World Hello
    print(reverse("  Hi There.  "))   # There. Hi
    print(reverse(123))               # Error


if __name__ == "__main__":
    main()
