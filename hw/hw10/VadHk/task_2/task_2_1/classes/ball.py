class Ball:
    def __init__(self, ball_type="regular"):
        self.ballType = ball_type

    def __str__(self):
        return f"Ball type: {self.ballType}"