def rect_area (x,y):
    '''Rectangle area'''
    return x*y

def triangle_area(base, height):
    '''Triangle area'''
    return base*height/2

def circle_area(r):
    '''Circle area'''
    return round(3.14*r,2)

choice = int(input('Enter 1, 2 or 3 for Rectangle, Triangle or Circle area calculation '))

match choice:
    case 1:
        x = float(input ('Enter width '))
        y = float(input ('Enter height '))
        print(rect_area(x,y))
    case 2:
        x = float(input ('Enter base '))
        y = float(input ('Enter height '))
        print(triangle_area(x,y))
    case 3:
        x = float(input ('Enter radius '))
        print(circle_area(x))
