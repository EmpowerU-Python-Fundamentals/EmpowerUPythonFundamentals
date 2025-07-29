"""Function that return the largest number of two numbers and robust to user input"""

def get_num (a):
    while True:
        try:
            return float(input(a).replace(',', '.'))
        except ValueError:
            print ("This is not a number. Please try again")
        
a = get_num ("Enter first number: ")
b = get_num ("Enter second number: ")

def largest_num (a, b):
    if a > b:
      return a
    elif b > a:
      return b
    else:
      return ("Numbers are equal")

result = largest_num (a, b)
print(result)
