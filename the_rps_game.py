import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

class TheRPSGame():
    def get_user_selection(self):
        user_input = input("Enter a choice (rock[0], paper[1], scissors[2]): ")
        selection = int(user_input)
        action = Action(selection)
        return action

    def get_computer_selection(self):
        selection = random.randint(0, len(Action) - 1)
        action = Action(selection)
        return action

