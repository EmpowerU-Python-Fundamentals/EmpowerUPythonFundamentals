class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def create():
    return [Man(), Woman()]


if __name__ == '__main__':
    print(create())

