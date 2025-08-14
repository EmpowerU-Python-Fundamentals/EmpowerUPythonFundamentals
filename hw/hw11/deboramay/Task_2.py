def get_day_of_week():
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    try:
        number = int(input("Enter a number (1-7): "))
        print(days[number])
    except ValueError:
        print("Error: You must enter a number!")
    except KeyError:
        print("Error: Number must be between 1 and 7!")

get_day_of_week()
