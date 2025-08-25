"""My way of solving task 3"""


class Human:
    """Base class: Human"""
    pass


class Man(Human):
    """Subclass: Man"""
    pass


class Woman(Human):
    """Subclass: Woman"""
    pass


def create():
    """Return an array of length 2 containing objects (representing Adam and Eve)"""
    return [Man(), Woman()]
