def rectanlegle_area(length, width):
    '''Rectangle area'''
    return length * width

def triangle_area(base, height):
    '''Triangle area'''
    return (base * height) / 2

def circle_area(radius):
    '''Circle area'''
    return round(3.14 * radius ** 2, 2)

choise = int(input('Enter 1, 2 or 3 for Rectangle, Triangle or Circle area calculation: '))

match choise:  
    case 1:
        length = float(input('Enter length: '))
        width = float(input('Enter width: '))
        print(rectanlegle_area(length, width))
    case 2:
        base = float(input('Enter base: '))
        height = float(input('Enter height: '))
        print(triangle_area(base, height))
    case 3:
        radius = float(input('Enter radius: '))
        print(circle_area(radius))
