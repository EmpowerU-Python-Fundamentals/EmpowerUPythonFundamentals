# I. Write a function that returns the largest of two numbers
def largest_func(first, second):
    """A function that returns the largest of two numbers"""
    if first > second:
        print(first)
    else:
        print(second)


# largest_func(3, 3)

# -----------------------------------------------------------------------------------------


# II. Write a program that calculates the area of a rectangle, triangle and circle(write three functions to calculate
# the area. And call them in the main program depending on the user’s choice)

def area_triangle(a, h):
    s = 0.5 * a * h
    return round(s)


def area_rectangle(a, b):
    s = a * b
    return s


def area_circle(r):
    s = 3.14 * r ** 2
    return s


def main_func():
    """The main function to call one of the other three to calculate the area of shapes."""
    invite = input(
        "Hi. Which area you want to calculate? Enter 't' for  triangle, 'r' for rectangle, 'o' for circle:  ")
    if invite == 't':
        a_input = input("Enter a: ")
        h_input = input("Enter h: ")
        return area_triangle(int(a_input), int(h_input))

    elif invite == 'r':
        a_input = input("Enter a: ")
        b_input = input("Enter b: ")
        return area_rectangle(int(a_input), int(b_input))

    elif invite == 'o':
        r_input = input("Enter r: ")
        return area_circle(int(r_input))

    else:
        return "Invalid input"


# print(main_func())

# -----------------------------------------------------------------------------------------


# III. write a function that calculates the number of characters included in given string
# input : «hello»
# output: {«h»:1, «e»:1, «|»:2, «o»:1}

def char_calc(st: str):
    """The function that calculates the number of characters included in given string."""
    result = {}
    low_st = st.lower()
    while True:
        for x in low_st:
            count = low_st.count(x)
            result[x] = count
        break
    return result


# print(char_calc("Hello"))
