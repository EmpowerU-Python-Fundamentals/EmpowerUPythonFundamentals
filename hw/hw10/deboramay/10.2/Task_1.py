#Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
#If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

#Test:
print(Ball().ball_type)
print(Ball('super').ball_type)