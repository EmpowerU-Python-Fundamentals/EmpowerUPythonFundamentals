# 1. Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny,
# and would like to greet him slightly different. She added a special case to her function, but she made a mistake.

# def greeting(name):
#     if name == "Johnny":
#         print("Hello Johnny, I love you!")
#     else:
#         print(f"Hello {name}, have a nice day!")


# 2. Given two ordered pairs calculate the distance between them.
# Round to two decimal places. This should be easy to do in 0(1) timing.

# def distance(x1, y1, x2, y2):
#     distance = ((x2-x1)**2+(y2-y1)**2)**0.5
#     return round(distance, 2)


# 3. Write a function taking in a string like WOW this is REALLY          amazing and returning
# Wow this is really amazing. String should be capitalized and properly spaced. Using re and string is not allowed.

# def convert(string):
#     spaces = " ".join(string.split())
#     final = spaces.capitalize()
#     return final

# 4. We need a function that can transform a number (integer) into a string.
#
# What ways of achieving this do you know?
#
# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"

# def transform(integer):
#     string = str(integer)
#     return string

# 5. You need to write a function that reverses the words in a given string. Words are always separated by a single space.
#
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

# def reverse(string):
#     spaces = string.strip()
#     l = spaces.split()
#     l1 = []
#     for w in l[::-1]:
#         l1.append(w)
#     result = " ".join(l1)
#     return result

# 6. In this kata you will create a function that takes in a list and returns a list with the reverse order.

# def rev(list):
#     new_list = []
#     for i in list[::-1]:
#         new_list.append(i)
#     return new_list

# 7. If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
#
# Additionally, if the number is negative, return 0.
#
# Note: If a number is a multiple of both 3 and 5, only count it once.

# def result(n):
#     s = 0
#     if n < 0:
#         s = 0
#     else:
#         for num in range(0, n):
#             if num % 3 == 0 or num % 5 == 0:
#                 s += num
#     return s


# 8. You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is
# running out and the nearest pump is 50 miles away! You know that on average,
# your car runs on about 25 miles per gallon. There are 2 gallons left.
#
# Considering these factors, write a function that tells you if it is possible to get to the pump or not.
#
# Function should return true if it is possible and false if not.

# def if_poss(dist, m_per_gal, gal):
#     remains = m_per_gal * gal - dist
#     if remains < 0:
#         return False
#     else:
#         return True


# 9. Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
#
# The function takes a name as its only argument, and returns one of the following strings:
#
# name + " plays banjo"
# name + " does not play banjo"
# Names given are always valid strings.

# def banjo(name):
#     name0 = name.lower()
#     if name0[0] == "r":
#         return f"{name} plays banjo"
#     else:
#         return f"{name} does not play banjo"


# 10. Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

# def conv(value):
#     if value == True:
#         return "Yes"
#     elif value == False:
#         return "No"

# 11. Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts
# the number of sheep present in the array (true means present).

# def count(l):
#     num = 0
#     for i in l:
#         if i:
#             num += 1
#     return num

# 12. Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right
# tails. To help her, you must correct the broken function to make sure that the second argument (tail),
# is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
#
# If the tail is right return true, else return false.
#
# The arguments will always be non empty strings, and normal letters.

# def correct_tail(body, tail):
#     if body[-1] == tail:
#         return True
#     else:
#         return False