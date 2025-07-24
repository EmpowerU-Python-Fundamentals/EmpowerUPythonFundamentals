def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    return False
print(correct_tail("Fox", "x"))
print(correct_tail("Emu", "t"))