class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

ball1 = Ball()
ball2 = Ball("super")

#regular
print(ball1.ball_type)
#super
print(ball2.ball_type)
