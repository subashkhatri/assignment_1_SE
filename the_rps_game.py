import random
from enum import IntEnum
import sys


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


class TheRPSGame:
    WIN_COUNT = 5

    def __init__(self):
        self.user_win_count = 0
        self.computer_win_count = 0

    def get_user_selection(self):
        print(f"**********Welcome to the ROCK PAPER SCISSORS GAME********")
        for i in range(2):
            self.next_line()
        print("********** Select your choice in between 0 - 2 ********")
        user_input = input(
            "*********Enter a choice (rock[0], paper[1], scissors[2]) or press (q) to quit the game: "
        )
        if user_input.lower() == "q":
            sys.exit()
        selection = int(user_input)
        action = Action(selection)
        return action

    def get_computer_selection(self):
        selection = random.randint(0, len(Action) - 1)
        action = Action(selection)
        return action

    def check_winning_player(self, user_action, computer_action):
        if user_action == computer_action:
            for i in range(2):
                self.next_line()
            print(f"Both players selected {user_action.name}. It's a tie! \n")
        elif user_action == Action.Rock:
            if computer_action == Action.Scissors:
                for i in range(2):
                    self.next_line()
                self.user_win_count += 1
                print(f"Rock smashes scissors! You win this round!")
            else:
                for i in range(2):
                    self.next_line()
                self.computer_win_count += 1
                print(f"Paper covers rock! You lose.")
        elif user_action == Action.Paper:
            if computer_action == Action.Rock:
                for i in range(2):
                    self.next_line()
                self.user_win_count += 1
                print(f"Paper covers rock! You win!",  self.user_win_count)
            else:
                for i in range(2):
                    self.next_line()
                self.computer_win_count += 1
                print(f"Scissors cuts paper! You lose.")
        elif user_action == Action.Scissors:
            if computer_action == Action.Paper:
                for i in range(2):
                    self.next_line()
                self.user_win_count += 1
                print(f"Scissors cuts paper! You win!",  self.user_win_count)
            else:
                for i in range(2):
                    self.next_line()
                self.computer_win_count += 1
                print(f"Rock smashes scissors! You lose.")

    def is_game_won(self):
        if self.user_win_count == self.WIN_COUNT:
            for i in range(2):
                self.next_line()
                print(f"You won")
                self.next_line()
                return True
        elif self.computer_win_count == self.WIN_COUNT:
            for i in range(2):
                self.next_line()
                print(f"Computer won")
                self.next_line()
                return False
        else:
            None

    def next_line(self):
        print("********************************************************* \n")

    def main(self):
        print("Starting Game")
        self.run()

    def run(self):
        self.computer_win_count = 0
        self.user_win_count = 0

        while True:
            try:
                user_action = self.get_user_selection()
            except ValueError as e:
                range_str = f"[0, {len(Action) - 1}]"
                print(f"Invalid selection. Enter a value in range {range_str}")
                continue

            computer_action = self.get_computer_selection()
            self.check_winning_player(user_action, computer_action)
            game_result = self.is_game_won()

            breakpoint
            if game_result != None:
                break

        play_again = input("Play again? (y/n): ")
        if play_again.lower() == "y":
            self.main()


if __name__ == "__main__":
    # let's start the game here
    play = TheRPSGame()
    play.run()
