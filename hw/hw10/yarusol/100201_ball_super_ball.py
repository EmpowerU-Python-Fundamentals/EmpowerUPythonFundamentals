# Create a class Ball.
# Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, 
#   ball objects should instantiate with a "ball type" of "regular."

class Ball():
    def __init__(self, ball_type: any = None ):
        self.ball_type = "regular" if not ball_type else ball_type
