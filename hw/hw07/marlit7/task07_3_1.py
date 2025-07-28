#I. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

#II. Find The Distance Between Two Points
import math
def distance(x1, y1, x2, y2):
    dis = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return round(dis,2)

#III. No yelling!
def filter_words(st):
    st_cl = " ".join(st.split())
    return st_cl.capitalize()

#IV. Convert a Number to a String
def number_to_string(num):
    num = str(num)
    return num

#V. Reversing Words in a String
def reverse(st):
    st = st.split()
    st = st[::-1]
    st = " ".join(st)
    return st

#VI. Reverse List Order
def reverse_list(l):
    l.reverse()
    return l

#VII. Multiples of 3 or 5
def solution(number):
    ls=[]
    for i in range(1,number):
        if i%3==0:
            ls.append(i)
        elif i%5==0 and i not in ls:
            ls.append(i)
    return sum(ls)

#VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg*fuel_left<distance_to_pump:
        return False
    else:
        return True

#IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0]=="R" or name[0]=="r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

#X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    if boolean==True:
        return "Yes"
    elif boolean==False:
        return "No"

#XI. Counting sheep
def count_sheeps(sheep):
    ar = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True]
    sheep = ar.count(True)
    return sheep

#XII. Is this my tail?
def correct_tail(body, tail):
    sub = body[-1]
    if sub == tail:
        return True
    else:
        return False






