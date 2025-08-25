# task1
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# task2
def distance(x1, y1, x2, y2):
    return round(((x2-x1)**2 + (y2-y1)**2) ** 0.5, 2)

# task3
def filter_words(st):
    return ' '.join(st.capitalize().split())

# task4
def number_to_string(num):
    return str(num)

# task5
def reverse(st):
    return ' '.join(st.split()[::-1])

# task6
def reverse_list(l):
    return l[::-1]

# task7
def solution(number):
    if number < 1:
        return 0
    number = number - 1
    summult = lambda a: (a + (number // a) * a) / 2 * (number // a)
    return summult(3) + summult(5) - summult(15)

# task8
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

# task9
def are_you_playing_banjo(name):
    if name[0] == 'r' or name[0] == 'R':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

# task10
def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'

# task11
def count_sheeps(sheep):
    return sheep.count(True)

# task12
def correct_tail(body, tail):
    return body[-1] == tail
