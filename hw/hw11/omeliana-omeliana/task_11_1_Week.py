def day_of_the_week():
    """

    Analyzes the entered number and returnes the day of the week.
    """
    week = { 
        1: "Mon",
        2: "Teu",
        3: "Wen",
        4: "Thu",
        5: "Fri",
        6: "Sat",
        7: "Sun"
    }

    try:
        day = int(input("Enter the number of the day 1-7: "))
        if day in week:
            print(f"This day is: {week[day]}")
        else:
            print("Enter day from 1 to 7! ")
    except ValueError:
        print("You entered not a number!")

day_of_the_week()