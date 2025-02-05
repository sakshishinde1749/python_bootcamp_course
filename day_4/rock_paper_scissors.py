import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]


user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n'))
if user_choice >=0 and user_choice <= 2:
    print(f"\n{game_images[user_choice]}")
else:
    print("Please choose number between 0 to 2")

computer_choice = random.randint(0, 2)
print(f"\nComputer choice:\n{game_images[computer_choice]}\n")


if user_choice >= 3 or user_choice < 0:
    print("You typed invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif user_choice < computer_choice:
    print("You lose!")
elif user_choice == computer_choice:
    print("Its a draw")

