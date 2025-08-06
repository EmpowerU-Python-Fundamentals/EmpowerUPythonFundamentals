import math

#Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

#Simple: Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)

#No yelling!
def filter_words(st):
    words = st.split()
    cleaned = [word.lower() for word in words]
    cleaned[0] = cleaned[0].capitalize()
    return ' '.join(cleaned)

#Convert a Number to a String!
def number_to_string(num):
    return str(num)

#Reversing Words in a String
def reverse(st):  
    words = st.strip().split()
    words.reverse()
    return ' '.join(words)

#Reverse List Order
def reverse_list(l):
    return l[::-1]

#Multiples of 3 or 5
def solution(number):
    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


#Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

#Are You Playing Banjo?
def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

#Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

#Counting sheep...
def count_sheeps(sheep):
    return sheep.count(True)

#Is this my tail?
def correct_tail(body, tail):
    sub = body[len(body)-len(tail)]
    if sub == tail:
        return True
    else:
        return False
