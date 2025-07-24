import math


# tasks part 1 
def task_p1_1(a = 1, b = 2):
    print(f'Largest between {a} and {b} is {max(a, b)}')

def task_p1_2(a = 5, h = 10):
    print(f"Area of the triangle is {0.5 * a * h}")
    print(f"Area of the rectangle is {a * h}")
    print(f"Area of the circle is {3.14 * (a / 2) ** 2}")

def task_p1_3(word = "hello"):
    print(f'The word "{word}" has {len(word)} characters.')
    for char in set(word):
        print(f'{char}: {word.count(char)}')

# tasks part 2
# https://www.codewars.com/kata/55225023e1be1ec8bc000390/javascript
def task_p2_1(name = "Johnny"):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# https://www.codewars.com/kata/simple-find-the-distance-between-two-points
def task_p2_2(x1 = 1.0, y1 = 1.0, x2 = 1.0, y2 = 1.0):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(round(distance, 2))

# https://www.codewars.com/kata/no-yelling
def task_p2_3(string = "WOW this is REALLY          amazing"):
    updated_string = ' '.join(string.strip().capitalize().split())
    print(updated_string)

# https://www.codewars.com/kata/convert-a-number-to-a-string
def task_p2_4(number):
    print(str(number))

# https://www.codewars.com/kata/reversing-words-in-a-string
def task_p2_5(string = "This is an example"):
    print(' '.join(string.split()[::-1]))

# https://www.codewars.com/kata/reverse-list-order
def task_p2_6(array = [1, 2, 3, 4, 5]):
    print(array[::-1])

# https://www.codewars.com/kata/multiples-of-3-or-5
def task_p2_7(number = 10):
    if number < 0:
        return 0
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

# https://www.codewars.com/kata/will-you-make-it
def task_p2_8(distance_to_pump, mpg, fuel_left):
    print(mpg * fuel_left >= distance_to_pump)

# https://www.codewars.com/kata/are-you-playing-banjo
def task_p2_9(name = "Ringo"):
    if name[0].lower() == "r":
        print(f'{name} + plays banjo')
    else:
        print(f'{name} + does not play banjo')

# https://www.codewars.com/kata/convert-boolean-values-to-strings-yes-or-no
def task_p2_10(boolean = True):
    print("Yes" if boolean else "No")

# https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/python
def task_p2_11(sheeps = [True, True, False, True, True, True, False, True, False, True]):
    sheep_count = 0
    for sheep in sheeps:
        if sheep:
            sheep_count += 1
    return sheep_count

# https://www.codewars.com/kata/is-this-my-tail/train/python
def task_p2_12(body, tail):
    print(body[-1] == tail)