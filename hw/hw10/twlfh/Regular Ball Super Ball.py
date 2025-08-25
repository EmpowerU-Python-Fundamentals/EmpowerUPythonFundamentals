class Ball:
    def __init__(self, type_ball='regular'):
        self.type_ball = type_ball

    @property
    def ball_type(self):
        return self.type_ball



ball1 = Ball()
ball2 = Ball("super")
print(ball1.ball_type)
print(ball2.ball_type)