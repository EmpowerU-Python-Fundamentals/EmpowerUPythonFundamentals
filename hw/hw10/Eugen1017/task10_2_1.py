class Ball(object):
    def __init__(self, ball_type="regular"):
        self.__ball_type = ball_type

    @property
    def ball_type(self):
        return self.__ball_type

    @ball_type.setter
    def ball_type(self, ball_type):
        self.__ball_type = ball_type

