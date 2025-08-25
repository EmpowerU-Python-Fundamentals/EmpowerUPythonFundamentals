import area

def main():
    """
    To calculate the desired area, provide arguments as follows:
    
    for rectangle (a, b - sides):
    r <a> <b>
   
    fot triangle (h - altitude, b - base):    
    t <h> <b>
    
    for circle (r - radius):    
    c <r>
    
    """
          
    print(main.__doc__)
    choice = input("Write your arguments:\n").strip().lower().split()

    # Error messages
    default = "Invalid argument(s) provided."
    quantity = "Invalid quantity of arguments provided."
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
            result = area.rectangle(a, b)
            
        case "t":
            if len(choice) != 3:
                exit(quantity)
            try:
                h, b = float(choice[1]), float(choice[2])
            except (TypeError, ValueError):
                exit(default)
            if any(el <= 0 for el in (h, b)):
                exit(zero)
            result = area.triangle(h, b)
            
        case "c":
            if len(choice) != 2:
                exit(quantity)
            try:
                r = float(choice[1])
            except (TypeError, ValueError):
                exit(default)
            if r <= 0:
                exit(zero)
            result = area.circle(r)
            
        case _:
            exit(default)
            
    print(result)
        
    
if __name__ == "__main__":
    main()
