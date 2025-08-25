# Code written by Ivan Savytsky
# Code reviewed for PEP 8 compliance by ChatGPT


def are_you_playing_banjo(name):
    """Return banjo message based on name starting with 'R' or 'r'."""
    if not isinstance(name, str):
        return "Enter a valid name."

    if name.startswith(("R", "r")):
        return f"{name} plays banjo"
    return f"{name} does not play banjo"


def main():
    print(are_you_playing_banjo("Rick"))   # Rick plays banjo
    print(are_you_playing_banjo("Adam"))   # Adam does not play banjo


if __name__ == "__main__":
    main()
