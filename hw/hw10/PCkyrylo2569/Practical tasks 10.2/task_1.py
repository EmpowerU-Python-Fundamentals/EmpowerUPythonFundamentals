class Ball():
    def __init__(self, ballType="regular"):
        self.ballType = ballType

ball1 = Ball()
ball2 = Ball("super")

print(ball1.ballType)
print(ball2.ballType)