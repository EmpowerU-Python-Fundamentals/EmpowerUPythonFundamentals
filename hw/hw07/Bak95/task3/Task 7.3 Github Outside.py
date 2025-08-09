# 1. Jenny's greeting
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

print("1.", greet("Johnny"))           # Hello, my love!

# 2. Distance between two ordered pairs
def distance(p1, p2):
    return round(((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5, 2)

print("2.", distance((0, 0), (3, 4)))  # 5.0

# 3. Filter words
def filter_words(st):
    words = st.split()
    fixed = ' '.join(words).lower()
    return fixed.capitalize()

print("3.", filter_words('WOW this is REALLY          amazing'))  # Wow this is really amazing

# 4. Transform number to string
def number_to_string(num):
    return str(num)

print("4.", number_to_string(123))    # "123"
print("4.", number_to_string(-100))   # "-100"

# 5. Reverse words in string
def reverse_words(text):
    return ' '.join(text.strip().split()[::-1])

print("5.", reverse_words("Hello World"))     # World Hello
print("5.", reverse_words("Hi There."))       # There. Hi

# 6. Reverse list
def reverse_list(l):
    return l[::-1]

print("6.", reverse_list([1, 2, 3, 4]))        # [4, 3, 2, 1]

# 7. Sum of multiples of 3 or 5
def solution(number):
    if number < 0:
        return 0
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

print("7.", solution(10))                     # 23

# 8. Can you reach the pump?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

print("8.", zero_fuel(50, 25, 2))             # True
print("8.", zero_fuel(100, 25, 2))            # False

# 9. Are you playing banjo?
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name[0].lower() == 'r' else f"{name} does not play banjo"

print("9.", are_you_playing_banjo("Rick"))    # Rick plays banjo
print("9.", are_you_playing_banjo("Paul"))    # Paul does not play banjo

# 10. Boolean to "Yes"/"No"
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

print("10.", bool_to_word(True))              # Yes
print("10.", bool_to_word(False))             # No

# 11. Count sheep
def count_sheeps(sheep):
    return sum(1 for s in sheep if s == True)

sheep_list = [True, True, False, True, None, False, True]
print("11.", count_sheeps(sheep_list))        # 4

# 12. Correct tail
def correct_tail(body, tail):
    return body[-1] == tail

print("12.", correct_tail("Fox", "x"))        # True
print("12.", correct_tail("Lion", "t"))       # False