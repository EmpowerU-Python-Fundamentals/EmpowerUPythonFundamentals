"""day of the week"""
DAYS = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

def day_of_the_week(number: int) -> str:
    """finds day of the week by number
    Args:
        number (int): input number
    Raises:
        ValueError: if it is not a number or more than 7
    Returns:
        str: day of the week
    """
    if number > 7 or number < 0:
        raise ValueError
    else:
        return DAYS[number]

def main():
    """main function"""
    try:
        input_number = int(input())
        print(day_of_the_week(input_number))
    except ValueError:
        print('Error: Incorrect. It`s must be positive number and no more than 7.')

main()
