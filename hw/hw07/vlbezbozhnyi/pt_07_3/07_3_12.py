def correct_tail(body, tail):
    sub = body[len(body) - len(tail) :]
    return sub == tail
