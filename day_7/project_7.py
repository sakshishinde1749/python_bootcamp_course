# Guess the word, HANGMAN project

import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["apple", "sakshi", "shinde", "happy", "success"]

chosen_word = random.choice(word_list)
print(chosen_word)

game_over = False
correct_letters = []
live = 0

while not game_over:
    guess = input("Guess the word: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    print(display)

    if guess not in chosen_word and live <= 6:
        live += 1
        print(stages[live])
    else:
        print(stages[live])

    if "_" not in display and live <= 6:
        game_over = True
        print("You win!")
    elif live == 6:
        game_over = True
        print("You die!")
    





