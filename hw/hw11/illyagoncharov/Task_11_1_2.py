days ={1: "Monday",
       2: "Tuesday",
       3: "Wednesday",
       4: "Thursday",
       5: "Friday",
       6: "Saturday",
       7: "Sunday"
       }
day = input("Enter the number of day: ")

try:
    print(days[int(day)])
except ValueError:
    print("Incorrect data")
except KeyError:
    print("Day must be in range 1-7")