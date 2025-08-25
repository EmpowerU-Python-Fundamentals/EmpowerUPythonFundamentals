def day_of_the_week(number):
    days={
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday",
        7:"Sunday"

    }
    if 1 <= number >=7:
        print("Number must be between 1 and 7")
    else:
        print ("Day of week:", days[number])

try:
    user_input=input("Enter a number 1-7 for day of the week")
    num=int(user_input)
    day_of_the_week(num)
except ValueError:
    print("Invalid input. Please enter a number.")
