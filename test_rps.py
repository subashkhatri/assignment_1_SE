import unittest
from the_rps_game import TheRPSGame

from unittest.mock import patch
from enum import IntEnum


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


# @patch('builtins.print')
class UnitTestRPSGame(unittest.TestCase):
    def test_paper_wins_against_rock(self):
        # rock[0], paper[1], scissors[2]
        the_rps_game = TheRPSGame()
        user_action = 1
        computer_action = 0
        the_rps_game.check_winning_player(user_action, computer_action)
        assert the_rps_game.user_win_count == 1

    def test_rock_wins_against_scissor(self):
        the_rps_game = TheRPSGame()
        user_action = 0
        computer_action = 2
        the_rps_game.check_winning_player(user_action, computer_action)
        assert the_rps_game.user_win_count == 1

    def test_scissor_wins_against_paper(self):
        the_rps_game = TheRPSGame()
        user_action = 2
        computer_action = 1
        the_rps_game.check_winning_player(user_action, computer_action)
        assert the_rps_game.user_win_count == 1

    def test_computer_randomly_picks_options(self):
        # breakpoint()
        the_rps_game = TheRPSGame()
        assert (the_rps_game.get_computer_selection() != None) == True

    def test_winner_gets_one_point(self):
        the_rps_game = TheRPSGame()
        user_action = 2
        computer_action = 1
        the_rps_game.check_winning_player(user_action, computer_action)
        assert the_rps_game.user_win_count == 1
        assert the_rps_game.computer_win_count == 0

    def test_game_is_won_with_five_points(self):
        the_rps_game = TheRPSGame()
        the_rps_game.user_win_count = 4
        the_rps_game.computer_win_count = 0
        assert the_rps_game.is_game_won() != True

        the_rps_game.user_win_count = 5
        assert the_rps_game.is_game_won() == True


if __name__ == "__main__":
    unittest.main()
