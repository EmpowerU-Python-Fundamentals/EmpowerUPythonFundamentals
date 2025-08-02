def number_to_day():
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
        num_input = input("Enter a number from 1 to 7: ")
        num = int(num_input)
        if num in days:
            print(f"The day is: {days[num]}")
        else:
            print("Invalid number! Please enter a number between 1 and 7.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        
number_to_day()