def correct_tail(body, tail):
    """
    Checks if the last character of the given 'body' string matches the 'tail' character, case-insensitively.
    """
    sub = body[len(body)-1]
    if sub.lower() == tail.lower():
        return True
    else:
        return False