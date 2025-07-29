# I. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# II. Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)

# III. No yelling!
def filter_words(st):
    return " ".join(st.split()).capitalize()

# IV. Convert a Number to a String
def number_to_string(num):
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    return str(num)

# V. Reversing Words in a String
def reverse(st):
    return " ".join(st.split()[::-1])

# VI. Reverse List Order
def reverse_list(l):
    """return a list with the reverse order of l"""
    return l[::-1]

# VII. Multiples of 3 or 5
def solution(number):
    """Return sum of multiples of 3 or 5 below the given number."""
    if number < 1:
        return 0
    else:
        return sum(i for i in range(3, number) if i % 3 == 0 or i % 5 == 0)

# VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg <= 0:
        return False
    return distance_to_pump / mpg <= fuel_left

# IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    return name + (" plays banjo" if name and name.lower().find('r') == 0 else " does not play banjo")

# X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# XI. Counting sheep
def count_sheeps(sheep):
    return sheep.count(True) if sheep else 0

# XII. Is this my tail?
def correct_tail(body, tail):
    return body.endswith(tail)