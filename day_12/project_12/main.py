from art import logo
import random

print(logo)

print("Welcome to the Word Guessing Game!")
print("I am thinking of a number between 1 and 100.\n")

chosen_num = random.randint(1, 100)

user_response = input("Choose difficulty. Type 'easy' or 'hard': ").lower()

def guess_finder(number_of_guess):
    guess_count = number_of_guess
    print(f"\nYou have {number_of_guess} attempts to guess the number")

    for _ in range(1, number_of_guess+1):
        guess = int(input("Make a guess: "))

        if guess == chosen_num:
            print("You win! 🎉")

        else:
            guess_count -= 1
            if guess_count == 0 and guess != chosen_num:
                print(f"😞 You Lose! the answer is {chosen_num}")

            elif guess < chosen_num:
                print(f"Too low. guess again\nyou have {guess_count} attempts remaining to guess the number")

            elif guess > chosen_num:
                print(f"Too high\nguess again\nyou have {guess_count} attempts remaining to guess the number")

            else:
                print("🚫 Pls type valid number")


if user_response == 'easy':
    guess_finder(10)

elif user_response == 'hard':
    guess_finder(5)

else:
    print("🚫 Pls type valid word")




