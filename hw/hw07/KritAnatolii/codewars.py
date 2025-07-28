
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
