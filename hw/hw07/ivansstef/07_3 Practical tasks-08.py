# Code written by Ivan Savytsky
# Code reviewed for PEP 8 compliance by ChatGPT


def can_reach_pump(distance_to_pump, mpg, fuel_left):
    """Return True if car can reach the pump, else False."""
    try:
        distance_to_pump = float(distance_to_pump)
        mpg = float(mpg)
        fuel_left = float(fuel_left)
    except ValueError:
        return "All inputs must be numbers."

    return mpg * fuel_left >= distance_to_pump


def main():
    print(can_reach_pump(50, 25, 2))   # True
    print(can_reach_pump(60, 25, 2))   # False


if __name__ == "__main__":
    main()
