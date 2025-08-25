# import re
#
#
# pattern = r"^(?:admin|employee)(?:-id|id|-)[0-9]+$"
#
# def check(login):
#     if re.fullmatch(pattern, login, re.IGNORECASE):
#         return True
#     else:
#         raise ValueError(f"incorrect login '{login}'")
#
#
# def divide(numerator: float, denominator: float):
#     try:
#         return f'Result is {numerator / denominator}'
#     except ZeroDivisionError:
#         return f'Oops, {numerator}/{denominator}, division by zero is error!!!'
#     except (ValueError, TypeError):
#         return 'Value Error! You did not enter a number!'
#
#
# def check_age(age):
#         if age <= 0:
#             raise ValueError('Incorrect')
#
# while True:
#     try:
#         age = int(input())
#         check_age(age)
#         print(age)
#         break
#     except ValueError:
#         continue
#
#
# class InputError(Exception):
#     def __init__(self, data):
#         self.data = data
#
#     def check(self):
#         if not isinstance(self.data, str):
#             raise InputError('Type text error')
#         elif len(self.data) < 3:
#             raise InputError("Short text error")
#         elif len(self.data) > 15:
#             raise InputError('Long text error')
#         return True
#
# def check(text):
#     t = InputError(text)
#     return t.check()
#
#
# class MyError:
#      def __init__(self, message):
#          self.message = message
#
#      def __str__(self):
#          return self.message
#
# def check_positive(number):
#      try:
#          val = float(number)
#      except ValueError:
#          return MyError('Error type: ValueError!')
#      if val < 0:
#          return MyError(f'You input negative number: {float(number)}. Try again.')
#
#      return f'You input positive number: {float(number)}'
#
#
# print(isinstance(check_positive("-235"), MyError))
#
# def check_odd_even(number):
#     try:
#         if number %2 == 0:
#             return 'Entered number is even.'
#         else:
#             return 'Entered number is odd.'
#     except TypeError:
#         return 'You entered not a number.'
#
# print(check_odd_even('qeq'))