import re

DAYS = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}

class DayError(Exception):
    def __init__(self, msg):
        self.__msg = msg

    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, value):
        self.__msg = value

    def __str__(self):
        return self.msg

def get_day(num):
    if not re.match(r"^[+-]?\d+$", num):
        raise DayError("Please enter a numeric value")
    elif int(num) < 1 or int(num) > 7:
        raise DayError("Days must be in range 1-7")

    return DAYS.get(int(num))


def main():
    while True:
        try:
            day_week = input("Enter a num of weeks day: ")
            print(f"the day is {get_day(day_week)}")
            return
        except DayError as e:
            print(e)
            continue

if __name__ == "__main__":
    main()