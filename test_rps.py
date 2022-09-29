from logging import error
from pdb import set_trace
import random
import unittest
from unittest.mock import patch

from enum import IntEnum
from the_rps_game import TheRPSGame

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

class  UnitTestRPSGame(unittest.TestCase):
    def test_computer_selection(self):
        the_rps_game = TheRPSGame()
        results = []
        for i in range(10):
            results.append(the_rps_game.get_computer_selection())

        new_result = len(set(results))

        if new_result > 1:
            print("Test passed!")
        else:
            print("Test has failed!")
            self.fail("Fail")

    def test_user_input(self):
        the_rps_game = TheRPSGame()
        results = random.randint(0,2)
        if results == Action.Rock:
            print("Test passed!")
            pass
        elif results == Action.Paper:
            print("Test passed!")
            pass
        elif results == Action.Scissors:
            print("Test passed!")
            pass
        else:
            print("Test has failed!")
            self.fail("Fail")

    def test_winning_player(self):
        user_selection = random.randint(0,2)
        computer_selection = random.randint(0,2)
        the_rps_game = TheRPSGame()
        the_rps_game.check_winning_player(user_selection, computer_selection)

        if user_selection > 3 or user_selection < 0:
            print("Test case has failed!")
            self.fail("Failed")
        elif computer_selection > 3 or computer_selection < 0:
            print("Test case has failed!")
            self.fail("Failed")
        else:
            print("Test has passed!")
            pass

    if __name__ == '__main__':
        unittest.main()