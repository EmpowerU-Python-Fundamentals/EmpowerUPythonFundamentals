def find_largest(a, b):
    if a > b:
        return a
    else:
        return b
print("Largest:", find_largest(6, 12))  

def largest(a, b):
    
    if any(not isinstance(el, (int, float)) for el in (a, b)):
        try:
            a = float(a)
            b = float(b)
        except (ValueError, TypeError):
            exit("Should be integers or floats to compare")
            
    if a == b:
        result = "Equal"
    elif a > b:
        result = a
    else:
        result = b
    return result


