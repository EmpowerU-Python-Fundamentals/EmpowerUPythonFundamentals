weekday = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

class IncorrectWeekday(ValueError):
    pass

def askWeekday():
    try:
        day = int(input('Enter a number of day in a week: '))
        if 0 <= day <= 7:
            return day
        else:
            raise IncorrectWeekday
    except (IncorrectWeekday, ValueError):
        return None

def run():
    day = askWeekday()
    while not day:
        print('Day should be a natural number less than 8')
        day = askWeekday()
    print(day, 'in a week is', weekday[day])

if __name__ == '__main__':
    run()
