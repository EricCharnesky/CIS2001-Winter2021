from unittest import TestCase
from ball import Ball

class TestBall(TestCase):
    def test_hi_there(self):
        self.fail()

    def test_toss(self):
        # Arrange, Act, Assert

        # Arrange - setup variables for testing
        ball = Ball("")
        expected_is_moving = True

        # Act - call the code we are testing, and get an actual result
        ball.toss()
        actual_is_moving = ball.get_is_moving()

        # Assert - did we get what we expected
        self.assertEqual(expected_is_moving, actual_is_moving)

    def test_catch(self):
        # Arrange, Act, Assert

        # Arrange - setup variables for testing
        ball = Ball("")
        expected_is_moving = False

        # Act - call the code we are testing, and get an actual result
        ball.catch()
        actual_is_moving = ball.get_is_moving()

        # Assert - did we get what we expected
        self.assertEqual(expected_is_moving, actual_is_moving)

    def test_get_type_of_ball(self):
        # Arrange, Act, Assert

        # Arrange - setup variables for testing
        expected_type_of_ball = "round"
        ball = Ball(expected_type_of_ball)

        # Act - call the code we are testing, and get an actual result
        actual_type_of_ball = ball.get_type_of_ball()

        # Assert - did we get what we expected
        self.assertEqual(expected_type_of_ball, actual_type_of_ball)
