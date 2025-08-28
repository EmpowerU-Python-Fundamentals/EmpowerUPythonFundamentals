def compare(first, second):
    """this function compares two numbers"""
    if first > second:
        print(first)
    else:
        print(second)

def rectangle_area(a,b):
    """this function returns an area of a rectangle"""
    return a*b

def triangle_area(a,h):
    """this function returns an area of a triangle, where a is base and h is a height"""
    return (a*h)/2

def circle_area(r):
    """this function returns an area of a circle, where r is a radius"""
    return 3.14*r*r

def number_of_characters(word):
    d = {}
    for ch in word:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    print(d)
number_of_characters("hello")

