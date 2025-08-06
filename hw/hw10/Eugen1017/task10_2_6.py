from curses.ascii import isupper

illegal_identifier_chars = [
    ' ', '-', '!', '@', '#', '$', '%', '^'
    '&', '*', '(', ')', '+', '=', '[', ']',
    '{', '}', '|', '\', ', ': ', '\'',
    '"', ',', '.', '<', '>', '?', '~', '`'
]
def validate_name(func):
    def wrapper(cls, name):
        if not isupper(name[0]) or not name:
            raise ValueError("Invalid name")
        if any((True for c in name if c in illegal_identifier_chars)):
            raise ValueError("Invalid name")
        return func(cls, name)
    return wrapper

@validate_name
def class_name_changer(cls, new_name):
    cls.__name__ = new_name
    return cls


