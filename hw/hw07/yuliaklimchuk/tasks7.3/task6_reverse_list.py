# In this kata you will create a function that takes in a list and returns a list with the reverse order.

def reverse_list(l):
    reversed_list = l[::-1]
    return reversed_list

print(reverse_list([1,2,3,4]))