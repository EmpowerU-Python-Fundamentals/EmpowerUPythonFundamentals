def get_possible(miles: int, gallons: int) -> bool:
    miles_per_gallon = 25

    if miles - miles_per_gallon * gallons < 0:
        return False

    return True


print(get_possible(miles=50, gallons=2))