class Ball:
    def __init__(self, ball_type = "regular"):
        self._ball_type = ball_type

    @property
    def ball_type(self):
        return self._ball_type


if __name__ == '__main__':
    ball1 = Ball()
    ball2 = Ball("super")
    print(ball1.ball_type)
    print(ball2.ball_type)
