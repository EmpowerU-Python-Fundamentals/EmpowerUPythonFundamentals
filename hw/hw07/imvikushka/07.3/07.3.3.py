# No yelling!

def filter_words(st):
    first_char = st[0].upper()
    rest = st[1:].lower()
    new_str = first_char + rest
    return " ".join(new_str.split())