DAYS = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"}


def main():
    day_num = input("Provide a number for a day (1 - 7): ")
    try:
        num = int(day_num)
        if 1 <= num <= 7:
            print(f"The number you've entered, {num}, corresponds to {DAYS[num]}.")
        else:
            raise ValueError
    except (ValueError, TypeError):
        exit("Please, provide an integer between 1 ... 7")
    
        
if __name__ == "__main__":
    main()