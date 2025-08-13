def get_day_of_the_week():

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    input_day = input("Enter a number (1 - Monday, 2 - Tuesday, 3 - Wednesday, 4 - Thursday, 5 - Friday, 6 - Saturday, 7 - Sunday): ")

    try:
        index = int(input_day)
        print(f"The day corresponding to number {index} is: {days[index-1]}")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")

    except IndexError as error:
        print(f"Index error: {error}")


if __name__ == "__main__":
    get_day_of_the_week()