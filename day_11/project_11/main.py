from art import blackjack_logo
import random


user_response = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

your_cards = []
computer_cards = []
your_score = sum(your_cards)
computer_score = sum(computer_cards)


print(blackjack_logo)

your_cards = your_cards.extend(random.sample(cards, 2))
print(f"Your cards: {your_cards}, current score: {your_score}\n")

computer_cards = computer_cards.extend(random.sample(cards, 1))
print(f"Computer\'s first card: {computer_cards[0]}\n")

user_response = input("Type 'y' to get another cards, type 'n' to pass: ")

if user_response == 'y':
    your_cards = your_cards.extend(random.sample(cards, 1))
    print(f"Your cards: {your_cards}, current score: {your_score}\n")   

    