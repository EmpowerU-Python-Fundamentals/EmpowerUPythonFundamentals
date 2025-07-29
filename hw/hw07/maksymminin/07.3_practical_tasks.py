# Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"

# Simple: Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    d = (dx * dx + dy * dy) ** 0.5
    return round(d, 2)

#No yelling!
def filter_words(s):
    words = s.split()
    cleaned = [word.lower() for word in words]
    if cleaned:
        cleaned[0] = cleaned[0].capitalize()
    return ' '.join(cleaned)

#Convert a Number to a String!
def number_to_string(num):
    return str(num)

#Reversing Words in a String
def reverse(st):
    trimmed = st.strip()
    words = trimmed.split()
    reversed_words = words[::-1]
    st = ' '.join(reversed_words)
    return st

#Reverse List Order
def reverse_list(l):
    return l[::-1]

#Multiples of 3 or 5
def solution(number):
    if number < 0:
        return 0
    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

#Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    max_distance = mpg * fuel_left
    return max_distance >= distance_to_pump

#Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    return name

#Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"

#Counting sheep...    
def count_sheeps(sheep):
    count = 0
    for s in sheep:
        if s is True:
            count += 1
    return count
pass

#Is this my tail?
def correct_tail(body, tail):
    sub = body[-1]
    if sub == tail:
        return True
    else:
        return False