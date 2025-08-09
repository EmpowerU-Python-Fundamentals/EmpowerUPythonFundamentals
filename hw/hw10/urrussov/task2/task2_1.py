class Ball:
    """A class representing a ball with a specific type."""

    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type

    def __str__(self):
        return self.ball_type