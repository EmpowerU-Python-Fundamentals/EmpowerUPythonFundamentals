"""checking age"""
def check_age(age: int) -> str:
    """checks age
    Args:
        age (int): _description_
    Raises:
        ValueError: if age is negative
    Returns:
        str: message about age
    """
    if age < 0:
        raise ValueError('Your age is negative')
    elif age % 2 == 0:
        return 'Your age is even'
    else:
        return 'Your age is odd'

def main():
    """main function"""
    try:
        age_input = int(input())
        print(check_age(age_input))
    except ValueError as e:
        print(f"Error: {e}")

main()
