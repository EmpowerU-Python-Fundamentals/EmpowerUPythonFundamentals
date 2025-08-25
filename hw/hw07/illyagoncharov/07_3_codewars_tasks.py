"""Task1 Jenny's secret message"""
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"


"""Task2  Find The Distance Between Two Points"""
def distance(x1, y1, x2, y2):
    res = pow(x2-x1, 2) + pow(y2-y1, 2)
    return round(pow(res, 0.5), 2)


"""Task3  No yelling!"""
def filter_words(st):
    return " ".join(st.split()).capitalize()


"""Task4 Convert a Number to a String"""
def number_to_string(num):
    return str(num)


"""Task5  Reversing Words in a String"""
def reverse(st):
    star = st.split()[::-1]
    st = " ".join(star)
    return st


"""Task6  Reverse List Order"""
def reverse_list(l):
    return l[::-1]


"""Task7 Multiples of 3 or 5"""
def solution(number):
    res = 0
    for i in range(number):
        if i%3 == 0 or i%5 == 0:
            res = res+i
    return res


"""Task8 Will you make it?"""
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump<=mpg*fuel_left


"""Task9 Are You Playing Banjo?"""
def are_you_playing_banjo(name):
    if name.lower()[0] == "r":
        return name + " plays banjo"
    return name + " does not play banjo"


"""Task10 Convert boolean values to strings 'Yes' or 'No’"""
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    return "No"


"""Task11 Counting sheep"""
def count_sheeps(sheep):
    return sum([x for x in sheep if x])

"""Task12 Is this my tail?"""
def correct_tail(body, tail):
    return body[-1:] == tail