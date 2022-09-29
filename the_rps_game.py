import random
from enum import IntEnum

class Action(IntEnum):
	Rock = 0
	Paper = 1
	Scissors = 2


class TheRPSGame:
	WIN_COUNT = 5
	def get_user_selection(self):
			user_input = input("Enter a choice (rock[0], paper[1], scissors[2]): ")
			selection = int(user_input)
			action = Action(selection)
			return action

	def get_computer_selection(self):
			selection = random.randint(0, len(Action) - 1)
			action = Action(selection)
			return action

	def check_winning_player(self, user_action, computer_action):
		if user_action == computer_action:
			print(f"Both players selected {user_action.name}. It's a tie!")
		elif user_action == Action.Rock:
			if computer_action == Action.Scissors:
				print("Rock smashes scissors! You win!")
				self.user_win_count += 1
			else:
				print("Paper covers rock! You lose.")
				self.computer_win_count += 1
		elif user_action == Action.Paper:
			if computer_action == Action.Rock:
				print("Paper covers rock! You win!")
				self.user_win_count += 1
			else:
				print("Scissors cuts paper! You lose.")
				self.computer_win_count += 1
		elif user_action == Action.Scissors:
			if computer_action == Action.Paper:
				print("Scissors cuts paper! You win!")
				self.user_win_count += 1
			else:
				print("Rock smashes scissors! You lose.")
				self.computer_win_count += 1

	def main(self):

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
				if self.user_win_count == self.WIN_COUNT:
					print(f"You won")
					break
				elif self.computer_win_count == self.WIN_COUNT:
					print(f"Computer won")
					break


		play_again = input("Play again? (y/n): ")
		if play_again.lower() == "y":
			self.main()



# let's start the game here
play = TheRPSGame()
play.main()
