# Code written by Ivan Savytsky
# Code reviewed for PEP 8 compliance by ChatGPT


def correct_tail(body, tail):
    """Return True if tail matches last letter of body."""
    if not isinstance(body, str) or not isinstance(tail, str):
        return "Inputs must be strings."

    return body[-1] == tail


def main():
    print(correct_tail("fox", "x"))     # True
    print(correct_tail("lion", "t"))    # False


if __name__ == "__main__":
    main()
