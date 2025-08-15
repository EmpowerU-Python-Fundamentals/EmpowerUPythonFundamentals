
# # I - Jenny's secret message
# def greet(name):
#     return "Hello, my love!" if name.lower() == "johnny" else f"Hello, {name}!"
# # ===============================================================================


# # II - Find The Distance Between Two Points
# from math import sqrt

# def distance(point1, point2):
#     print()
#     print(f"Distance between points: {sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2):.2f}\n")

# def coordinates():
#     return tuple(map(float, input("Enter coordinates (x, y): ").strip().split(',')))

# while True:
#     try:
#         point1 = coordinates()
#         point2 = coordinates()
#         distance(point1, point2)
#         break
#     except (ValueError, IndexError):
#         print("\n>>>>>>>             Invalid input              >>>>>>>\n>>>>>>>   Please enter numeric X & numeric Y   >>>>>>>\n")
# # ===============================================================================


# # III - No yelling!

# def filter_words(no_yelling):
#     return " ".join(no_yelling.split()).capitalize()
# # ===============================================================================


# # IV - Convert a Number to a String!
# def number_to_string(num):
#     return str(num) if isinstance(num, (int, float)) else print("Enter a number to function")
    # # return f'"{n}"' # if you want to return a string with quotes
# # ===============================================================================


# # V - Reversing Words in a String
# def reverse(sentence):
#     return ' '.join(sentence.strip().split()[::-1])


# # V - Reverse the Order of Words in a Sentence 1.0 - wide version
# import re

# def reverse(text: str):
#     sentences = re.findall(r'[^.!?]+[.!?]?', text, re.UNICODE)
#     print()
#     print('sentences:   ', sentences)
#     reversed = []

#     for sentence in sentences:
#         stripped = sentence.strip()
#         print('stripped:    ', stripped)
#         if not stripped:
#             continue

#         punctuation = stripped[-1] if stripped[-1] in '.!?' else ''
#         words = stripped.rstrip('.!?').strip().split()[::-1]
#         print('words:       ', words)
#         if not words:
#             continue

#         first_word = words[0]
#         words[0] = first_word[0].upper() + first_word[1:] if len(first_word) > 1 else first_word.upper()
#         last_word = words[-1]
#         words[-1] = last_word[0].lower() + last_word[1:] if len(last_word) > 1 else last_word.upper()

#         joined = ' '.join(words) + punctuation
#         print('joined:      ', joined)
#         print('punctuation: ', punctuation)

#         reversed.append(joined)
#         print('new_sentence:', reversed)
#         print()

#     return ' '.join(reversed)

# reverse("Hello world! How are you? I am fine. Let's go to the park.")
# # ===============================================================================


# # VI - Reverse List Order
# def reverse_list(lst):
#     return lst[::-1]
# # ===============================================================================


# # VII - Multiples of 3 or 5
# def sum_mult_3_or_5(number):
#     if number < 0:
#         return 0
#     return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)
# # ===============================================================================


# # VIII - Will you make it?
# def get_to_pump():
#     while True:
#         try:
#             distance = float(input("\nEnter distance to the pump (in miles):                  "))
#             mpg = float(input("Enter your car's fuel efficiency (in miles per gallon): "))
#             fuel = float(input("Enter the amount of fuel in your tank (in gallons):     "))
#             print()
#             if mpg * fuel < distance:
#                 print("\n>>>>>>>>>>>       Sorry. Not enough fuel to reach the pump       >>>>>>>>>>>>\n")
#             else:
#                 print(f'Congratulations! You can reach the pump. Your distance: {mpg * fuel} km \n')
#         except ValueError:
#             print("\n>>>>>>>>>>>       Invalid input       >>>>>>>>>>>>\n>>>>>>>>>>>   Please enter numeric values   >>>>>>>>>>>>\n")
#             continue

#         return mpg * fuel >= distance

# get_to_pump()
# # ===============================================================================


# # IX - Are You Playing Banjo?
# def banjo_check():
#     name = input("Enter your name: ")
#     if not isinstance(name, str):
#         return "Invalid input: name must be a string"
#     else:
#         print(f"{name} plays banjo" if name.lower().startswith('r') else f"{name} does not play banjo")

# banjo_check()
# # ===============================================================================


# # X - Convert boolean values to strings 'Yes' or 'No'.

# def bool_to_word(boolean: bool) -> str:
#     return "Yes" if boolean else "No"
# # ===============================================================================


# # XI - Counting sheep...
# def count_sheeps(sheep):
#     return sum(1 for i in sheep if i)

# flock_of_sheep = [True,  True,  True,  False,
#                   True,  True,  True,  True ,
#                   True,  False, True,  False,
#                   True,  False, False, True ,
#                   True,  True,  True,  True ,
#                   False, False, True,  True]
# print(f"Number of sheep: {count_sheeps(flock_of_sheep)}")
# # ===============================================================================


# # XII - Is this my tail?
def correct_tail(body, tail):
    return 1 if body[-len(tail):] == tail else 0

print(correct_tail("Fox", "x"))