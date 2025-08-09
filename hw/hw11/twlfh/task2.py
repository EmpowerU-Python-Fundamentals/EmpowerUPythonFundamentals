def date():
    try:
        user_input = input('Enter a number from 1 to 7:')
        if not user_input.isdigit():
            raise ValueError('You must enter a number from 1 to 7')

        num = int(user_input)
        result = day_of_week(num)
        return result
    except ValueError as e:
        return e

def day_of_week(num):
    if num < 1 or num > 7:
        raise ValueError('Enter a number from 1 to 7')
    else:
        days = {
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Saturday',
            7: 'Sunday'
        }
    return days[num]

print(date())