class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

ball1 = Ball()
ball2 = Ball("super")

print("Тип м’яча 1:", ball1.ball_type)
print("Тип м’яча 2:", ball2.ball_type)
