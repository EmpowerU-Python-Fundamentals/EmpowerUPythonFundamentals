def main():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    try:
        number_input = input("Enter the number of the day of the week: \n")
        number = int(number_input)
        if number<=0:
            raise IndexError
        print (days_of_week[number-1])
    except ValueError:
        print (f"You have entered not a number: {number_input}")
    except IndexError:
        print (f"You have entered incorrect number: {number}") 

        
if __name__ == "__main__":
    main()