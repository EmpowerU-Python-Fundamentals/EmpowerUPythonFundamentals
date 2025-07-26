#!/usr/bin/env python3
def calc_characters_in_string(string: str) -> dict:
    result = dict()
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

user_input = input("enter a string\n")
print(calc_characters_in_string(user_input))