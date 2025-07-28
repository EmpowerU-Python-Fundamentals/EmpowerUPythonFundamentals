
#I. Jenny's secret message
def greet(name):
    if name != 'Johnny':
        return f"Hello, {name}!"
    else:
        return 'Hello, my love!'


#II. Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return round(distance, 2)

#III. No yelling!
def filter_words(st):
    res = " ".join(st.split().capitalize())
    return res

#IV. Convert a Number to a String
def number_to_string(num):
    return str(num)

#V. Reversing Words in a String
def reverse(st):
    st = st.split()
    st.reverse()
    return ' '.join(st)

#VI. Reverse List Order
def reverse_list(l):
    return l[::-1]

#VII. Multiples of 3 or 5
def solution(number):
    if number <= 0:
        return 0
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)

#VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if fuel_left * mpg >= distance_to_pump else False

#IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        answer = " plays banjo" 
    else:
        answer = " does not play banjo"
    return name + answer

#X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

#XI. Counting sheep
def count_sheeps(sheep):
    count = 0
    for sh in sheep:
        if sh == True:
            count +=1
    return count

#XI. Counting sheep
def count_sheeps(sheep):
    return sheep.count(True)

#XII. Is this my tail?
def correct_tail(body, tail):
    sub = body[-1]
    if sub == tail:
        return True
    else:
        return False
