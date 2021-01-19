class Ball:

    def __init__(self, type_of_ball):
        self._type_of_ball = type_of_ball
        self._is_moving = False

    def toss(self):
        self._is_moving = True

    def catch(self):
        self._is_moving = False

    def get_is_moving(self):
        return self._is_moving

    def get_type_of_ball(self):
        return self._type_of_ball

    def __str__(self):
        if self._is_moving:
            return f'{self._type_of_ball} is moving, you better catch it!'
        return f'{self._type_of_ball} is in your hand...'

