# Code written by Ivan Savytsky
# Code reviewed for PEP 8 compliance by ChatGPT


def count_sheeps(sheep_list):
    """Return count of present sheep (True values)."""
    if not isinstance(sheep_list, list):
        return "Input must be a list."

    return sum(1 for sheep in sheep_list if sheep is True)


def main():
    sheep = [
        True, True, False, None, True, False, True, True,
        True, True, None, False, True, True, False, True
    ]
    print(count_sheeps(sheep))    # 11


if __name__ == "__main__":
    main()
