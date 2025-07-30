from math import pi


def rectangle_area(params:dict):
    """The function calculates the area of a rectangle"""
    return round(params['a']*params['b'], 2)


def triangle_area(params:dict):
    """The function calculates the area of a triangle"""
    return round(0.5*params['a']*params['b'], 2)


def circle_area(params:dict):
    """The function calculates the area of a circle"""
    return round(pi*pow(params['a'], 2), 2)


area = {'Rectangle': rectangle_area, 'Triangle': triangle_area, 'Circle': circle_area}


def area_calculate(figure = None, params = None):
    res = area[figure]
    return res(params)