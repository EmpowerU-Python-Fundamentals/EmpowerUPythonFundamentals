# Code written by Ivan Savytsky
# Code reviewed for PEP 8 compliance by ChatGPT


def solution(number):
    """Return sum of all multiples of 3 or 5 below given number."""
    try:
        number = int(number)
    except ValueError:
        return "Invalid input. Enter an integer."

    if number < 0:
        return 0

    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)


def main():
    print(solution(10))    # 23
    print(solution(-5))    # 0


if __name__ == "__main__":
    main()
