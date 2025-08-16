def even_or_odd(number: int) -> str:
        if number < 0:
              raise ValueError(f"Your age {number} is less than zero, which is impossible")
        if number % 2 == 0:
            return f"Your age {number} is even"
        else:
            return f"Your age {number} is odd"
        
try:
      number = int(input("Enter your age to determine if it's even or odd\n"))
      print(even_or_odd(number))
except ValueError as e:
      print(e)