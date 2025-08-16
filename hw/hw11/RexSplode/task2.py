def name_day_of_week(ordinal: int) -> str:
    try:
        ordinal = int(ordinal)
        match ordinal:
            case 1: return "Monday"
            case 2: return "Tuesday"
            case 3: return "Wednesday"
            case 4: return "Thursday"
            case 5: return "Friday"
            case 6: return "Saturday"
            case 7: return "Sunday"
            case _: raise ValueError()

    except ValueError as e:
        return f"You entered '{ordinal}', and it is not a number from 1 to 7\n"


user_input = input("Enter a number from 1 to 7, and I'll give you the name of that day\n")
print(name_day_of_week(user_input))
