# I.Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

# II. Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round(((x1 - x2) ** 2 +(y2 - y1) ** 2) ** 0.5, 2)

# III. No yelling!
def filter_words(st):
    return ' '.join(st.lower().split()).capitalize()

# IV. Convert a Number to a String
def number_to_string(num):
    return str(num)

# V. Reversing Words in a String
def reverse(st):
    return ' '.join(reversed(st.split())).strip()

# VI. Reverse List Order
def reverse_list(l):
    return list(reversed(l))

# VII. Multiples of 3 or 5
def solution(number):
    if number < 0:
        return 0

    total_sum = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum

# VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg*fuel_left >= distance_to_pump

# IX. Are You Playing Banjo?
def areYouPlayingBanjo(name):
    if name.startswith('R') or name.startswith('r'):
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

# X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    if boolean:
        return 'Yes'
    else:
        return 'No'

# XI. Counting sheep
def count_sheeps(sheep):
    return sheep.count(True)

# XII. Is this my tail?
def correct_tail(body, tail):
      return body.endswith(tail)