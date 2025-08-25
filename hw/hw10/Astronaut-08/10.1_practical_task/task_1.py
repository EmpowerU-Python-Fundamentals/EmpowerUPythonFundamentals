'''This is DOC string'''
class Polygon:
    '''This is DOC string'''
    def __init__(self, side):
        self.side = side
        self.sides = [0 for i in range(self.side)]

    def inp_side(self):
        '''This is DOC string'''
        self.sides = [float(input(f'Enter side {str(i+1)}: ')) for i in range(self.side)]

class Rectangle(Polygon):
    '''This is DOC string'''
    def __init__(self):
        super().__init__(2)

    def square(self):
        '''This is DOC string'''
        a, b = self.sides
        print(f'The square of rectangle is: {a * b}')

r = Rectangle()
r.inp_side()
r.square()
