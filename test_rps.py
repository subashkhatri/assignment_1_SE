from logging import error
from pdb import set_trace
import unittest
from the_rps_game import TheRPSGame

class  UnitTestRPSGame(unittest.TestCase):
    def test_computer_selection(self):
        the_rps_game = TheRPSGame()
        results = []
        for i in range(10):
            results.append(the_rps_game.get_computer_selection())

        new_result = len(set(results))
        # set_trace()
        if new_result > 1:
            print("Pass")
        else:
            print("Fail")
            self.fail("shouldn't happen")

    if __name__ == '__main__':
        unittest.main()