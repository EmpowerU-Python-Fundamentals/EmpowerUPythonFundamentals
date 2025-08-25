#I. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

print(greet("Johnny")) 
print(greet("Max"))



#X. Convert boolean values to strings 'Yes' or 'No’

def bool_to_word(boolean):
    return "Yes" if boolean else "No"
print(bool_to_word(True))  
print(bool_to_word(False))

#XI. Counting sheep

def count_sheeps(sheep):
    return sum(1 for s in sheep if s is True)

#XII. Is this my tail?

def correct_tail(body, tail):
    last_char = body[len(body) - 1]
    if last_char == tail:
        return True
    else:
        return False

#II. Find The Distance Between Two Points

import math

def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(dist, 2)
print(distance(0, 0, 3, 4)) 
print(distance(1, 2, 4, 6))
#III. No yelling!

def filter_words(st):
    words = st.split()
    words = [word.lower() for word in words]
    if words:
        words[0] = words[0].capitalize()
        
    return ' '.join(words)
print(filter_words('HELLO CAN YOU HEAR ME'))           
print(filter_words('now THIS is REALLY interesting'))
print(filter_words('THAT was EXTRAORDINARY!'))
#IV. Convert a Number to a String

def number_to_string(num):
    return str(num)
print(number_to_string(999))  
print(number_to_string(-111))
#V. Reversing Words in a String

def reverse(text):
    words = text.strip().split()
    return ' '.join(words[::-1])
print(reverse("   Hello    World "))

#VI. Reverse List Order

def reverse_list(lst):
    return lst[::-1]
print(reverse_list([1, 2, 3, 4]))

#VII. Multiples of 3 or 5

def solution(n):
    if n < 0:
        return 0
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)
print(solution(10))   
print(solution(0))    
print(solution(-5))  
print(solution(20))

#VIII. Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump
print(zero_fuel(50, 25, 2)) 
print(zero_fuel(100, 25, 3))

#IX. Are You Playing Banjo?

def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    print(are_you_playing_banjo("Roman"))
    print(are_you_playing_banjo("Andrew"))

