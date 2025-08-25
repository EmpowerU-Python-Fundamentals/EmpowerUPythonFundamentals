class Human(object):
    def __init__(self) -> None:
        pass


class Man(Human):
    def __init__(self) -> None:
        pass


class Woman(Human):
    def __init__(self) -> None:
        pass


def God():
    return [Man(), Woman()]
