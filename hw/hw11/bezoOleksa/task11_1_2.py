day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

while True:
    try:
        inp = int(input('Enter a number of day in a week: '))
    except ValueError:
        print('Day in a week should be natural number less than 8')
        continue
    if inp < 0 or inp > 7:
        print('Day in a week should be natural number less than 8')
        continue
    print(f'{inp} day in a week is {day[inp]}')
    break
