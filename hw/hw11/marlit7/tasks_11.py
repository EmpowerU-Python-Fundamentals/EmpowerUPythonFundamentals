week={
    1:"понеділок",
    2:"вівторок",
    3:"середа",
    4:"четвер",
    5:"пятниця",
    6:"субота",
    7:"неділя",}

def day_week():

    try:
        num = int(input("День: "))
        if num in week:
            print(week[num])
        else:
            raise ValueError
    except ValueError:
        print("Немає такого дня тижня")

while True:
    day_week()