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

    def check_winning_player(self, user_action = 0, computer_action = 0):
        user_count, computer_count = 0, 0
        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
            user_count += 0
            computer_count += 0
        elif user_action == Action.Rock:
            if computer_action == Action.Scissors:
                print("Rock smashes scissors! You win!")
                user_count += 1
            else:
                print("Paper covers rock! You lose.")
                computer_count += 1
        elif user_action == Action.Paper:
            if computer_action == Action.Rock:
                print("Paper covers rock! You win!")
                user_count += 1
            else:
                print("Scissors cuts paper! You lose.")
                computer_count += 1
        elif user_action == Action.Scissors:
            if computer_action == Action.Paper:
                print("Scissors cuts paper! You win!")
                user_count += 1
            else:
                print("Rock smashes scissors! You lose.")
                computer_count += 1
