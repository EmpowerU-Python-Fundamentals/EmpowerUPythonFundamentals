import math

# I. Jenny's secret message
def greet(name):
    #return "Hello, {name}!".format(name=name)
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)
		
# II. Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2-x1)**2 + (y2-y1)**2), 2)
	
# III. No yelling!
def filter_words(st):
    normalized_text = ' '.join(st.strip().split())
    return normalized_text.capitalize()
	
# IV. Convert a Number to a String
def number_to_string(num):
    return str(num)
	
# V. Reversing Words in a String
def reverse(st):
    word_list = st.strip().split()
    return ' '.join(word_list[::-1])
	
# VI. Reverse List Order
def reverse_list(lst):
    return lst[::-1]
	
# VII. Multiples of 3 or 5
def solution(number):
    total_sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum
	
# VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    max_distance = mpg * fuel_left
    return max_distance >= distance_to_pump
		
# IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    first_letter = name[0].lower()
    if first_letter == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
		
# X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    return "Yes" if boolean else "No"
	
# XI. Counting sheep
def count_sheeps(sheep):
    sheep_count = 0
    for animal in sheep:
        if animal:
            sheep_count += 1
    return sheep_count
	
# XII. Is this my tail?
def correct_tail(body, tail):
    last_char = body[-1]
    return last_char == tail