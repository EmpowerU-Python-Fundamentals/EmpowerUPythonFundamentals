"""
2. Write a program that analyzes the entered number and, depending on the number,
gives the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). 
Take into account cases of entering numbers from 8 and more, 
as well as cases of entering non-numerical data.
"""

days_of_week = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

input = input("Enter a number from 1 to 7(Monday - Sunday): ")

try:
    if input.isdigit():
        day_number = int(input)
    else:
        raise TypeError("The entered value is not a number")
    if day_number < 0 or day_number > 7:
        raise ValueError("Number shuld be from 1 to 7.")
    else:
        print(days_of_week[day_number])
except (ValueError, TypeError) as e:
    print(e)
