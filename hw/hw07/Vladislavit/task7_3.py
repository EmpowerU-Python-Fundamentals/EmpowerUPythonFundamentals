#Task 1
def greet(name: str) -> str:
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

#Task 2
import math

def distance(x1, y1, x2, y2):
    return round(math.hypot(x2 - x1, y2 - y1), 2)

#Task 3
def filter_words(st):
    words = st.split()  
    sentence = " ".join(words).lower()  
    return sentence.capitalize()  

#Task 4
def number_to_string(num):
    return str(num)

#Task 5
def reverse(st):
    return " ".join(st.split()[::-1])

#Task 6
def reverse_list(l):
    return l[::-1]

#Task 7
def solution(n):
    if n <= 0:
        return 0
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)

#Task 8
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

#Task 9
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    return name + " does not play banjo"

#Task 10
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

#Task 11
def count_sheeps(sheep):
    return sum(1 for s in sheep if s is True)

#Task 12
def correct_tail(body, tail):
    return body[-1] == tail
