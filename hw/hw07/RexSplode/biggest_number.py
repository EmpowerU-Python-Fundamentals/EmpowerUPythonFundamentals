#!/usr/bin/env python3
def biggest_number(num1 : int, num2: int) -> int:
    """returns the biggest of two int numbers"""
    if not isinstance(num1, int) or not isinstance(num2, int):
        print("Those weren't int numbers, savvy?") 
        return 0
    num1, num2 = int(num1), int(num2)
    return num1 if num1 > num2 else num2

