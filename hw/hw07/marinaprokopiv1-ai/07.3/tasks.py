#TASK I.

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"


#TASK II.

import math

def distance(x1, y1, x2, y2):
    return round(math.hypot(x2 - x1, y2 - y1), 2)


#TASK III.

def filter_words(st):
    words = st.split()
    sentence = ' '.join(words).lower()
    
    return sentence.capitalize()


#TASK IV.

def number_to_string(num):
    return str(num)

#TASK V.

def reverse(s):
    return " ".join(s.split()[::-1])

#TASK VI.

def reverse_list(lst):
    return lst[::-1]


#TASK VII.

def solution(number):
    if number < 0:
        return 0
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)


#TASK VIII.

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

zeroFuel = zero_fuel


#TASK IX.

def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

#TASK X.

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

#TASK XI.

def count_sheeps(sheep):
    return sum(1 for s in sheep if s is True)

#TASK XII.

def correct_tail(body, tail):
    return body[-1] == tail