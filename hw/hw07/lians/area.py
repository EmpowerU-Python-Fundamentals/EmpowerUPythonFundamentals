import math

def main():
    """
    To calculate the desired area, provide arguments as follows:
    
    for rectangle:
    r <a> <b>
    
    fot triangle:
    t <a> <b> <c>
    
    for circle:
    c <r>
    
    where the a, b, c - sides, and r - radius.
    """
          
    print(main.__doc__)
    choice = input("Write your arguments:\n").strip().lower().split()

    # Error messages
    default = "Invalid argument_s provided."
    quantity = "Invalid quantity of argument_s provided."
    zero = "Zero or negative values are not valid."
    
    if not choice:
        exit(default)
        
    match choice[0]:
        case "r":
            if len(choice) != 3:
                exit(quantity)
            try:
                a, b = float(choice[1]), float(choice[2])
            except (TypeError, ValueError):
                exit(default)
            if any(el <= 0 for el in (a, b)):
                exit(zero)
            result = rectangle(a, b)
            
        case "t":
            if len(choice) != 4:
                exit(quantity)
            try:
                a, b, c = float(choice[1]), float(choice[2]), float(choice[3])
            except (TypeError, ValueError):
                exit(default)
            if any(el <= 0 for el in (a, b, c)):
                exit(zero)
            result = triangle(a, b, c)
            
        case "c":
            if len(choice) != 2:
                exit(quantity)
            try:
                r = float(choice[1])
            except (TypeError, ValueError):
                exit(default)
            if r <= 0:
                exit(zero)
            result = circle(r)
            
        case _:
            exit(default)
            
    print(result)
    

def rectangle(a, b):
    """Gives area of a rectangle with both sides given."""
    area = a * b
    return f"Area of a rectangle with the sides {a = }, {b = } is equal to {area:.2f}."


def triangle(a, b, c):
    """Gives area of a triangle with three sides given."""
    if not is_valid_tri(a, b, c):
        exit("Provided values do not correspond to a valid triangle.")
    s_per = (a + b + c) / 2
    area = math.sqrt(s_per * (s_per - a) * (s_per - b) * (s_per - c))
    return f"Area of a triangle with the sides {a = }, {b = }, {c = } is equal to {area:.2f}."


def is_valid_tri(a, b, c):
    """Checks if given sizes are valid by the triangle inequality rule."""
    max_side = max(a, b, c)
    is_triangle = (a + b + c - max_side) > max_side
    return is_triangle


def circle(r):
    """Gives area of a circle with radius given."""
    area =  math.pi * r**2
    return f"Area of a circle with the radius {r = } is equal to {area:.2f}."
    
    
if __name__ == "__main__":
    main()
