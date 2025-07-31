# Code written by Ivan Savytsky
# Code reviewed for PEP 8 compliance by ChatGPT


def reverse_list(items):
    """Return the reversed list."""
    if not isinstance(items, list):
        return "Input must be a list."

    return items[::-1]


def main():
    print(reverse_list([1, 2, 3, 4]))    # [4, 3, 2, 1]
    print(reverse_list("123"))          # Error


if __name__ == "__main__":
    main()
