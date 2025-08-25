#XII. Is this my tail?

def correct_tail(body, tail):
    last_char = body[len(body) - 1]
    if last_char == tail:
        return True
    else:
        return False

