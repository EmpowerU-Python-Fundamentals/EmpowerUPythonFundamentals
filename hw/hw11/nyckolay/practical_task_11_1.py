"""
Task 11.1. 

Write a program that prompts the user to enter their age, 
and then displays a message stating whether the age is even or odd. 

The program must provide the ability to enter a negative number, 
and in this case generate an exception. 
The master code should call a function that processes the information entered.
"""

def check_odd_even(age):
    "Check entered value for a number and even/odd"
    if age.isdigit():
        age = int(age)
        if age <= 0:
            raise ValueError("The entered number is negative")
        if age % 2 == 0:
            return "The number is even"
        else:
            return "The number is odd"
    else:
        raise TypeError("The entered value is not a number")

age = input("Enter your age: ")

print(check_odd_even(age))
