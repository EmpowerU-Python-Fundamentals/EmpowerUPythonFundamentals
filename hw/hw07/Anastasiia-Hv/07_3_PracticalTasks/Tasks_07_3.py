import math

#I. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"    
    return "Hello, {name}!".format(name=name)


#II. Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(dist, 2)


#III. No yelling!
def filter_words(text):
    words = [word for word in text.split(' ') if word != '']
    
    words = [word.lower() for word in words]
    
    if not words:
        return ''
    
    words[0] = words[0].capitalize()
    
    return ' '.join(words)


#IV. Convert a Number to a String
def number_to_string(num):
    return str(num)


#V. Reversing Words in a String
def reverse(st):
    return ' '.join(st.split()[::-1])


#VI. Reverse List Order
def reverse_list(l):
    return l[::-1]


#VII. Multiples of 3 or 5
def solution(number):
    if number <= 0:
        return 0
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


#VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump


#IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


#X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    return "Yes" if boolean else "No"


#XI. Counting sheep
def count_sheeps(sheep):
    count = 0
    for s in sheep:
        if s is True:
            count += 1
    return count


#XII. Is this my tail?
def correct_tail(body, tail):
    for i in range(len(tail)):
        if body[len(body) - len(tail) + i] != tail[i]:
            return False
    return True