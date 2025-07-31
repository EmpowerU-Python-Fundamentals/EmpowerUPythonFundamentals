                               #codewars tasks
#Jenny's secret message

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)
 
    
#Find The Distance Between Two Points

from math import sqrt
def distance(x1, y1, x2, y2):
    # Your code here
    return round(sqrt((x2-x1)**2 + (y2-y1)**2),2)


#No yelling! String should be capitalized and properly spaced. Using re and string is not allowed.
def filter_words(st):
    lst = st.split()
    result = ""
    for i in lst:
        result = result + i + " "
        
    return result.strip().capitalize()


#Convert a Number to a String!
def number_to_string(num):
    return f'{num}'
    #return str(num)     
    #return "{n}".format(n=num)
    
#Reversing Words in a String
def reverse(st):
    r = st.split()
    r = r[::-1]
    result = ""
    for i in r:
        result = result + i + " "
    st = result.strip()
    return st

#Reverse List Order
def reverse_list(l):
  return l[::-1]
  #return l.reverse()
  
#Multiples of 3 or 5
def solution(number):
    sum = 0
    if number < 0:
        return 0
    for i in range(number):
        if (i % 3) == 0 or (i % 5) == 0:
            sum += i
    return sum

#Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    return mpg * fuel_left >= distance_to_pump

#Are You Playing Banjo? If your name starts with the letter "R" or lower case "r", you are playing banjo!
def are_you_playing_banjo(name):
    # Implement me!
    if name[0] == 'R' or name[0] == 'r':
        return name + " plays banjo" 
    else:
        return name + " does not play banjo"
    
#Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    # TODO
    if boolean:
        return "Yes"
    else:
        return "No"
    
#Counting sheep... 
def count_sheeps(sheep):
  # TODO May the force be with you
    return sheep.count(True)

#Is this my tail? To help her, you must correct the broken function to make sure that the second argument (tail), 
# is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
def correct_tail(body, tail):
    sub = body[-1]
    if sub == tail:
        return True
    else:
        return False
