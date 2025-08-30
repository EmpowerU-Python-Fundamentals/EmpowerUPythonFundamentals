def convert_to_string(n):
    number = str(n)
    return f'"{number}"'
print(type(convert_to_string(12)))
print(convert_to_string(14.84))
print(convert_to_string(123))
print(convert_to_string(999))
print(convert_to_string(-100))