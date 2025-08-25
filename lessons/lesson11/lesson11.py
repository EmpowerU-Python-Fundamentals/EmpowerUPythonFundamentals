# a = int(input("a:"))
# b = int(input("b:"))
# print(a/b)
# print("end script")

# def f():

#     print("tets", value)

# g()

# 1 + "10"
# int("hsdvj")


# a = input("a:")
# b = input("b:")
# try:
#     a = int(a)
#     b = int(b)
#     print(a/b)
# except Exception as err:
#     print(f"ERROER {type(err)} {err}")

# print("end script")


# def input_two_int():
#     while True:
#         a = input("a:")
#         b = input("b:")
#         try:
#             a = int(a)
#             b = int(b)
#             return a, b
#         except Exception as err:
#             print(f"ERROER {type(err)} {err}")
# a, b = input_two_int()
# print(f"{a=} {b=}")
# print("end script")


# # Program to handle multiple errors with one except statement
# try:
#     a = int(input("Enter your number: "))
#     if a < 4:
#         b = a/(a-3) # throws ZeroDivisionError for a = 3
#     if a >= 4:
#         print("Value of b = ", b) # throws NameError
#     # note that braces () are necessary here for multiple exceptions
# except(ZeroDivisionError, NameError, ValueError) as err:
#     print("Error Occurred and Handled", type(err), err)

# print("end script")


# # Program to handle multiple errors with one except statement
# try:
#     a = int(input("Enter your number: "))
#     if a < 4:
#         b = a/(a-3) # throws ZeroDivisionError for a = 3
#     if a >= 4:
#         print("Value of b = ", b) # throws NameError
#     # note that braces () are necessary here for multiple exceptions
# except ZeroDivisionError:
#     print("ZeroDivisionError a-3 is 0")

# except NameError:
#     print("b is not define")
# except ValueError as err:
#     print("Error Occurred and Handled", type(err), err)
# except ArithmeticError:
#     print("ArithmeticError")
# except Exception:
#     print("Error")
# print("end script")



# def input_two_int():
#     print("start func")
#     while True:
#         a = input("a:")
#         b = input("b:")
#         try:
#             a = int(a)
#             b = int(b)
#         except ValueError:
#             print("\tretry")
#         except:
#             print(f"ERROER {type(err)} {err}")
#         else:
#             return a, b
#         print("Re Run fukc")
#     print("end func")
# a, b = input_two_int()
# print(f"{a=} {b=}")
# print("end script")


# def input_two_int():
#     print("start func")
#     while True:
#         a = input("a:")
#         b = input("b:")
#         try:
#             a = int(a)
#             b = int(b)
#             # a/b
#         except ValueError:
#             print("\tretry")
#         except:
#             print(f"ERROER {type(err)} {err}")
#         else:
#             return a, b
#         finally:
#             print("end func")
#         print("Re Run fukc")
# a, b = input_two_int()
# print(f"{a=} {b=}")
# print("end script")


# def f(a, b):
#     try:
#         print(a+b)
#         return a+b
#     finally:
#         print(a*b)
#         return a*b

# c = f(5, 3)
# print(f"{c=}")

# def input_number():
#     text = input("number: ")
#     if not text.isalnum():
#         raise ZeroDivisionError("number contain spec symbols:")
#         # raise "number contain spec symbols:" #TypeError: exceptions must derive from BaseException
#     return text

# while True:
#     input_number()


class CustomError(Exception):
    pass
    # def __init__(self, data):
    #     self.data = data
    # def __str__(self):
    #     return repr(self.data)

total_score = int(input("Enter expert score: "))
try:
    num_of_group = int(input("Enter number of your group: "))
    if num_of_group < 1:
        raise CustomError("Number of your group can't be less than 1")
except CustomError as e:
    print("We obtain error:", e)