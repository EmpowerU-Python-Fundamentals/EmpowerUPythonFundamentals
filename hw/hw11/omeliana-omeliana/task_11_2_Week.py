def get_weekday(number):
    """
    Function returns the day of a week according to the number.
    Number must be from 1 to 7.
    """
    week_dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    
    if number < 1 or number > 7:
        raise ValueError("Number must be between 1 and 7!")
    
    return week_dict[number]

def main():
    try:
        user_input = input("Enter a number for the day of the week (1-7): ")
        num = int(user_input)  # конвертуємо у число
        
        day_name = get_weekday(num)  # отримуємо назву дня
        print(f"The day corresponding to {num} is {day_name}.")
    
    except ValueError as e:
        print(f"Error: {e}. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()