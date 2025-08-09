'''This is DOC for task_2'''
week_day = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}

class WeekError(Exception):
    '''This is DOC for week error'''
    def __str__(self):
        return 'WeekError: Wrong number of week'

def check_day_of_week(day):
    '''This is the func'''
    try:
        day = int(day)
        if day in week_day.keys():
            return week_day.get(day)
        else:
            raise WeekError('invalid number of day')
    except ValueError as err:
        return f'{err} is not a day of week, invalid number'
    except WeekError as werr:
        return werr

print(check_day_of_week(input('Input number of day: ')))
