'''Practical tasks by Astronaut-08'''
import math
#TASK 1 Jenny's secret message
#Jenny has written a function that returns a greeting for a user.
#However, she's in love with Johnny, and would like to greet him slightly different.
#She added a special case to her function, but she made a mistake.
def greet(name):
    '''Greet message'''
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

#TASK 2 Find The Distance Between Two Points
#Given two ordered pairs calculate the distance between them.
#Round to two decimal places.
#This should be easy to do in 0(1) timing.
def distance(x1, y1, x2, y2):
    '''Рахує відстань між двома точками на площині'''
    return round(math.sqrt((x2-x1)**2 + (y2-y1)**2), 2)

#TASK 3 No yelling!
#Write a function taking in a string like WOW this is REALLY
#amazing and returning Wow this is really amazing.
#String should be capitalized and properly spaced.
#Using re and string is not allowed.
#Examples:
#filter_words('HELLO CAN YOU HEAR ME') #=> Hello can you hear me
#filter_words('now THIS is REALLY interesting') #=> Now this is really interesting
#filter_words('THAT was EXTRAORDINARY!') #=> That was extraordinary!
def filter_words(st):
    '''Нормалізує текст'''
    st = st.capitalize()
    return ' '.join(st.split())

#TASK 4 Convert a Number to a String!
#We need a function that can transform a number (integer) into a string.
#What ways of achieving this do you know?
#Examples (input --> output):
#123  --> "123"
#999  --> "999"
#-100 --> "-100"
def number_to_string(num):
    '''Перетворення в стрічку'''
    return str(num)

#TASK 5 Reversing Words in a String
#You need to write a function that reverses the words in a given string.
#Words are always separated by a single space.
#As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
#Example (Input --> Output)
#"Hello World" --> "World Hello"
#"Hi There." --> "There. Hi"
#Happy coding!
def reverse(st):
    '''Обертання стрічки'''
    return ' '.join(st.split()[::-1])

#TASK 6 Reverse List Order
#In this kata you will create a function that takes in a list and returns a list with the
#reverse order.
#Examples (Input -> Output)
#* [1, 2, 3, 4]  -> [4, 3, 2, 1]
#* [9, 2, 0, 7]  -> [7, 0, 2, 9]
def reverse_list(l):
    'Обертання ліста'
    return l[::-1]

#TASK 7 Multiples of 3 or 5
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6
#and 9. The sum of these multiples is 23.
#Finish the solution so that it returns the sum of all the multiples of 3 or 5 below
#the number passed in.
#Additionally, if the number is negative, return 0.
#Note: If the number is a multiple of both 3 and 5, only count it once.
def solution(number):
    '''Витягування з числа всіз 3 і 5 та сумування їх'''
    if number < 0:
        return 0
    sol = list()
    for i in range(number):
        if 0 < i < number and i % 3 == 0:
            sol.append(i)
        elif 0 < i < number and i % 5 == 0:
            sol.append(i)
    return sum(sol)

#TASK 8 Will you make it?
#You were camping with your friends far away from home, but when it's time to go back,
#you realize that your fuel is running out and the nearest pump is 50 miles away!
#You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons
#left.
#Considering these factors, write a function that tells you if it is possible to get to
#the pump or not.
#Function should return true if it is possible and false if not.
def zero_fuel(distance_to_pump, mpg, fuel_left):
    '''Рахує чи вистачить палива чи ні'''
    return True if distance_to_pump <= fuel_left * mpg else False

#TASK 9 Are You Playing Banjo?
#Create a function which answers the question "Are you playing banjo?".
#If your name starts with the letter "R" or lower case "r", you are playing banjo!
#The function takes a name as its only argument, and returns one of the following strings:
#name + " plays banjo"
#name + " does not play banjo"
#Names given are always valid strings.
def are_you_playing_banjo(name):
    '''Функція яка хоче щось спитати'''
    return name + ' plays banjo' if name[0].lower() == 'r' else name + ' does not play banjo'

#TASK 10 Convert boolean values to strings 'Yes' or 'No'.
#Complete the method that takes a boolean value and return a "Yes" string for true, or a
#"No" string for false.
def bool_to_word(boolean):
    '''Перетворення True в нормальний текст'''
    return 'Yes' if bool(boolean) else 'No'

#TASK 11 Counting sheep...
#Consider an array/list of sheep where some sheep may be missing from their place.
#We need a function that counts the number of sheep present in the array (true means present).
def count_sheeps(sheep):
    '''Порахуймо ж'''
    suma = 0
    for i in sheep:
        if i:
            suma += 1
    return suma

#TASK 12 Is this my tail?
#Some new animals have arrived at the zoo.
#The zoo keeper is concerned that perhaps the animals do not have the right tails.
#To help her, you must correct the broken function to make sure that the second argument (tail),
#is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
#If the tail is right return true, else return false.
#The arguments will always be non empty strings, and normal letters.
def correct_tail(body, tail):
    '''Виправелння функції'''
    if body[-1] == tail:
        return True
    else:
        return False
