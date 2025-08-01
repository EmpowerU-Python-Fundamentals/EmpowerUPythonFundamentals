# Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"


# Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)


# No yelling!

def filter_words(st):
    words = st.strip().split()
    if not words:
        return ''
    words = [w.lower() for w in words]
    words[0] = words[0].capitalize()
    return ' '.join(words)


# Convert a Number to a String!

def number_to_string(num):
    return str(num)


# Reversing Words in a String

def reverse(st):
    words = st.split()
    return ' '.join(words[::-1])


# Reverse List Order
def reverse_list(L):
    return list(reversed(L))


# Multiples of 3 or 5

def solution(number):
    if number <= 0:
        return 0

    def sum_m(x):
        y = (number - 1) // x
        return x * y * (y + 1) // 2

    return sum_m(3) + sum_m(5) - sum_m(15)


# Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump


# Are You Playing Banjo?
def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'


# Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    return "Yes" if boolean else "No"


# Counting sheep

def count_sheep(sheep):
    return sum(1 for i in sheep if i)


# Is this my tail?

def correct_tail(body, tail):
    return body[-1] == tail
