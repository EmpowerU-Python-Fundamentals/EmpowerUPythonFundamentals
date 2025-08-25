# 2. Write a program that analyzes the entered number
#   and, depending on the number, gives the day of the week
#   that corresponds to this number (1 is Monday, 2 is Tuesday, etc.).
# Take into account cases of entering numbers from 8 and more,
#   as well as cases of entering non-numerical data.

DAYS = {
    "1": "Monday",
    "2": "Tueasday",
    "3": "Wednesday",
    "4": "Thursday",
    "5": "Friday",
    "6": "Saturday",
    "7": "Sunday"
}

def number_to_week_day(text: str) -> str:
    return DAYS[text.strip()]

if __name__ == "__main__":
    try:
        text = input("Enter a week day number: ")
        print(f"It is {number_to_week_day(text)}.")
    except KeyError:
        print("It is not a valid week day number.")
        print("Enter a number from 1 to 7, please.")
    finally:
        print()