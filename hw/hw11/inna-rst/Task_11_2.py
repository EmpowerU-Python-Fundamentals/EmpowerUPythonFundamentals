class NotANumberError(Exception):
    pass


class DayOutOfRangeError(Exception):
    pass

def get_day_week_by_number(number):
    days_week = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday',
    }

    if number in days_week:
        return days_week[number]
    else:
        raise DayOutOfRangeError(f'Invalid number: {number}. Should be from 1 to 7.')

def is_integer_string(s):
    s = s.strip()
    if not s:
        return False
    if s[0] in '+-':
        body = s[1:]
        return len(body) > 0 and body.isascii() and body.isdigit()
    return s.isascii() and s.isdigit()

def main():
    while True:
        try:
            user_input = input('Enter a number from 1 to 7 (or "quit" to exit): ')

            if user_input.lower() == 'quit':
                print('Goodbye!')
                break

            if is_integer_string(user_input):
                number = int(user_input)
            else:
                raise NotANumberError(f"Error: '{user_input}' is not a valid integer. Use digits 1–7 (no letters or decimals).")

            day = get_day_week_by_number(number)
            print(f'Day {number}: {day}')
            break

        except DayOutOfRangeError as e:
            print(f"Error: {e}")
        except NotANumberError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == '__main__':
    main()